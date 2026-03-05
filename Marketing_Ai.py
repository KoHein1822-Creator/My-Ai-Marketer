import { useState, useRef, useEffect, useCallback } from "react";
import { AreaChart, Area, BarChart, Bar, LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

const C = {
  fb:"#6366f1",tt:"#ec4899",yt:"#ef4444",
  green:"#10b981",amber:"#f59e0b",blue:"#3b82f6",purple:"#8b5cf6",teal:"#14b8a6",
  bg:"#030712",card:"#111827",border:"#1f2937",sub:"#0d1117",
  muted:"#6b7280",dim:"#4b5563",text:"#e5e7eb",head:"#f9fafb",
};

const WK=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"];
const MO=["W1","W2","W3","W4"];
const YR=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
function genS(key,min,max,labels,off=0){return labels.map((name,i)=>({name,[key]:Math.max(min,Math.round(min+(max-min)*0.4+Math.sin((i+off)*0.9)*((max-min)*0.28)+Math.random()*(max-min)*0.24))}));}
function mkData(key,min,max){return{Weekly:{cur:genS(key,min,max,WK,0),prev:genS(key,Math.round(min*.78),Math.round(max*.84),WK,3)},Monthly:{cur:genS(key,min*4,max*4,MO,0),prev:genS(key,Math.round(min*3.1),Math.round(max*3.4),MO,2)},Yearly:{cur:genS(key,min*50,max*50,YR,0),prev:genS(key,Math.round(min*40),Math.round(max*43),YR,4)},Custom:{cur:genS(key,min*3,max*3,MO,1),prev:genS(key,Math.round(min*2.5),Math.round(max*2.7),MO,3)}};}
function sumS(arr,key){return arr.reduce((s,r)=>s+(r[key]||0),0);}
function fmt(n){if(n>=1e6)return(n/1e6).toFixed(1)+"M";if(n>=1000)return(n/1000).toFixed(1)+"K";return String(Math.round(n));}

const CLIENTS=["All Clients","Real Estate Co.","Fashion Brand","Restaurant Chain","Tech Startup","Beauty Studio"];
const PLATFORMS={
  Facebook:{color:C.fb,metrics:[
    [{key:"reach",label:"Reach",prefix:"",suffix:"",color:C.fb,data:mkData("reach",18000,95000)},{key:"impr",label:"Impressions",prefix:"",suffix:"",color:C.purple,data:mkData("impr",50000,250000)}],
    [{key:"engRate",label:"Engagement Rate",prefix:"",suffix:"%",color:C.teal,data:mkData("engRate",3,12)},{key:"clicks",label:"Post Clicks",prefix:"",suffix:"",color:C.blue,data:mkData("clicks",2000,14000)}],
    [{key:"vidViews",label:"Video Views",prefix:"",suffix:"",color:C.green,data:mkData("vidViews",40000,200000)},{key:"follows",label:"Page Follows",prefix:"",suffix:"",color:C.amber,data:mkData("follows",80,600)}],
  ]},
  TikTok:{color:C.tt,metrics:[
    [{key:"views",label:"Video Views",prefix:"",suffix:"",color:C.tt,data:mkData("views",80000,400000)},{key:"profile",label:"Profile Visits",prefix:"",suffix:"",color:C.purple,data:mkData("profile",4000,40000)}],
    [{key:"likes",label:"Likes",prefix:"",suffix:"",color:"#f472b6",data:mkData("likes",8000,80000)},{key:"shares",label:"Shares",prefix:"",suffix:"",color:C.blue,data:mkData("shares",2000,20000)}],
    [{key:"follows",label:"Followers Gained",prefix:"",suffix:"",color:C.green,data:mkData("follows",400,3000)},{key:"watch",label:"Watch Time (hrs)",prefix:"",suffix:"",color:C.teal,data:mkData("watch",2000,20000)}],
  ]},
  YouTube:{color:C.yt,metrics:[
    [{key:"views",label:"Views",prefix:"",suffix:"",color:C.yt,data:mkData("views",20000,150000)},{key:"impr",label:"Impressions",prefix:"",suffix:"",color:C.purple,data:mkData("impr",60000,500000)}],
    [{key:"watch",label:"Watch Time (hrs)",prefix:"",suffix:"",color:C.amber,data:mkData("watch",800,9000)},{key:"ctr",label:"CTR",prefix:"",suffix:"%",color:C.blue,data:mkData("ctr",2,8)}],
    [{key:"subs",label:"Subscribers",prefix:"+",suffix:"",color:C.green,data:mkData("subs",60,600)},{key:"revenue",label:"Est. Revenue",prefix:"$",suffix:"",color:C.teal,data:mkData("revenue",40,400)}],
  ]},
};
const mkStatus=(p,d,s,pub)=>({Pending:{count:p,items:Array.from({length:p},(_,i)=>`Content item #${i+1}`)},Drafting:{count:d,items:Array.from({length:d},(_,i)=>`Draft #${i+1}`)},Scheduled:{count:s,items:Array.from({length:s},(_,i)=>`Scheduled #${i+1}`)},Published:{count:pub,items:Array.from({length:pub},(_,i)=>`Published #${i+1}`)}});
const STATUS_DATA={"All Clients":{Facebook:mkStatus(8,5,6,19),TikTok:mkStatus(5,3,4,12),YouTube:mkStatus(3,2,3,8),All:mkStatus(16,10,13,39)},"Real Estate Co.":{Facebook:mkStatus(3,2,2,7),TikTok:mkStatus(1,1,1,3),YouTube:mkStatus(1,0,1,2),All:mkStatus(5,3,4,12)},"Fashion Brand":{Facebook:mkStatus(2,1,2,5),TikTok:mkStatus(2,1,2,5),YouTube:mkStatus(0,1,1,3),All:mkStatus(4,3,5,13)},"Restaurant Chain":{Facebook:mkStatus(1,1,1,4),TikTok:mkStatus(1,0,1,2),YouTube:mkStatus(0,0,0,1),All:mkStatus(2,1,2,7)},"Tech Startup":{Facebook:mkStatus(1,0,1,2),TikTok:mkStatus(1,1,0,1),YouTube:mkStatus(1,1,1,2),All:mkStatus(3,2,2,5)},"Beauty Studio":{Facebook:mkStatus(1,1,0,1),TikTok:mkStatus(0,0,0,1),YouTube:mkStatus(1,0,0,0),All:mkStatus(2,1,0,2)}};
const STATUS_META=[{key:"Pending",color:C.amber,bg:"#f59e0b12",icon:"⏳"},{key:"Drafting",color:C.fb,bg:"#6366f112",icon:"✍️"},{key:"Scheduled",color:C.blue,bg:"#3b82f612",icon:"📅"},{key:"Published",color:C.green,bg:"#10b98112",icon:"✅"}];
const NEWS_TABS=["Global News","Local News","Deep Insight","Weekly Report"];
const TAG_C={AI:"#6366f1",Marketing:"#f59e0b",TikTok:"#ec4899",YouTube:"#ef4444",Myanmar:"#10b981",Trend:"#3b82f6",Analysis:"#8b5cf6",Report:"#14b8a6"};
const NEWS={"Global News":[{tag:"AI",time:"2h ago",title:"OpenAI launches GPT-5 with real-time video understanding",src:"TechCrunch"},{tag:"Marketing",time:"4h ago",title:"Meta rolls out AI-generated ad creatives to all advertisers",src:"AdWeek"},{tag:"TikTok",time:"6h ago",title:"TikTok Shop surpasses $1B in weekly GMV globally",src:"Bloomberg"},{tag:"YouTube",time:"8h ago",title:"YouTube Shorts monetization expands to 100+ countries",src:"YouTube Blog"}],"Local News":[{tag:"Myanmar",time:"1h ago",title:"Facebook remains #1 digital marketing channel in Myanmar",src:"MMDigital"},{tag:"Trend",time:"3h ago",title:"Short-form video ads see 3x higher CTR in SEA markets",src:"SEA Report"},{tag:"Myanmar",time:"5h ago",title:"Mobile-first content drives 78% of brand discovery locally",src:"LocalInsight"}],"Deep Insight":[{tag:"Analysis",time:"Today",title:"Why Faceless content is outperforming branded content in 2025",src:"Strategy Weekly"},{tag:"Trend",time:"Yesterday",title:"The rise of AI agents in performance marketing workflows",src:"MarTech Report"}],"Weekly Report":[{tag:"Report",time:"This Week",title:"Top 10 viral content formats — Week 9, 2026",src:"AI Command Center"},{tag:"Report",time:"This Week",title:"Myanmar market trend summary: Feb 23 – Mar 1",src:"AI Command Center"}]};

function SegPicker({options,value,onChange,colorFn,small}){return(<div style={{display:"flex",background:"#0d1117",borderRadius:6,padding:2,gap:1}}>{options.map(o=>{const a=value===o,col=colorFn?colorFn(o):null;return <button key={o} onClick={()=>onChange(o)} style={{padding:small?"2px 7px":"3px 9px",borderRadius:4,border:"none",cursor:"pointer",fontSize:small?10:11,fontWeight:a?700:400,background:a?(col?col+"22":"#1f2937"):"transparent",color:a?(col||C.text):C.dim,whiteSpace:"nowrap"}}>{o}</button>;})}</div>);}
const TTip=({active,payload,label})=>{if(!active||!payload?.length)return null;return(<div style={{background:"#1a2235",border:`1px solid #374151`,borderRadius:6,padding:"7px 11px"}}><p style={{margin:"0 0 4px",color:C.muted,fontSize:10}}>{label}</p>{payload.map(p=><p key={p.dataKey} style={{margin:"2px 0",fontSize:11,color:p.color,fontWeight:700}}>{p.name==="prev"?"Prev: ":"Cur: "}{Number(p.value).toLocaleString()}</p>)}</div>);};
function CompareChart({curData,prevData,dataKey,color,chartType,compare}){const merged=curData.map((r,i)=>({name:r.name,cur:r[dataKey],...(compare&&prevData[i]?{prev:prevData[i][dataKey]}:{})}));const pCol=color+"70";const axes=<><XAxis dataKey="name" hide/><YAxis hide domain={["auto","auto"]}/><Tooltip content={<TTip/>}/></>;if(chartType==="Bar")return(<ResponsiveContainer width="100%" height={60}><BarChart data={merged} margin={{top:2,right:0,left:0,bottom:0}} barCategoryGap="20%">{axes}{compare&&<Bar dataKey="prev" name="prev" fill={pCol} radius={[2,2,0,0]} fillOpacity={0.45}/>}<Bar dataKey="cur" name="cur" fill={color} radius={[2,2,0,0]} fillOpacity={0.85}/></BarChart></ResponsiveContainer>);if(chartType==="Line")return(<ResponsiveContainer width="100%" height={60}><LineChart data={merged} margin={{top:2,right:0,left:0,bottom:0}}>{axes}{compare&&<Line dataKey="prev" name="prev" stroke={pCol} strokeWidth={1.2} dot={false} strokeDasharray="3 3"/>}<Line dataKey="cur" name="cur" stroke={color} strokeWidth={1.8} dot={false}/></LineChart></ResponsiveContainer>);return(<ResponsiveContainer width="100%" height={60}><AreaChart data={merged} margin={{top:2,right:0,left:0,bottom:0}}><defs><linearGradient id={`gc_${dataKey}`} x1="0" y1="0" x2="0" y2="1"><stop offset="5%" stopColor={color} stopOpacity={0.28}/><stop offset="95%" stopColor={color} stopOpacity={0}/></linearGradient><linearGradient id={`gp_${dataKey}`} x1="0" y1="0" x2="0" y2="1"><stop offset="5%" stopColor={pCol} stopOpacity={0.16}/><stop offset="95%" stopColor={pCol} stopOpacity={0}/></linearGradient></defs>{axes}{compare&&<Area dataKey="prev" name="prev" stroke={pCol} strokeWidth={1.2} fill={`url(#gp_${dataKey})`} dot={false} strokeDasharray="3 3"/>}<Area dataKey="cur" name="cur" stroke={color} strokeWidth={1.8} fill={`url(#gc_${dataKey})`} dot={false}/></AreaChart></ResponsiveContainer>);}
function MetricCard({m,tf,chartType,compare}){const d=m.data[tf]||m.data.Weekly;const cur=sumS(d.cur,m.key),prev=sumS(d.prev,m.key),diff=cur-prev,pct=prev>0?((diff/prev)*100):0,up=diff>=0;const fv=v=>m.prefix+fmt(v)+m.suffix;return(<div style={{background:C.card,border:`1px solid ${m.color}22`,borderRadius:10,padding:"12px 13px"}}><div style={{fontSize:10,color:C.dim,fontWeight:600,letterSpacing:0.4,marginBottom:4}}>{m.label.toUpperCase()}</div><div style={{display:"flex",alignItems:"flex-end",justifyContent:"space-between",marginBottom:compare?7:5}}><div style={{fontSize:20,fontWeight:800,color:C.head,lineHeight:1}}>{fv(cur)}</div><span style={{fontSize:10,padding:"2px 7px",borderRadius:99,background:up?"#10b98115":"#ef444415",color:up?C.green:"#ef4444",fontWeight:700}}>{up?"+":""}{pct.toFixed(1)}%</span></div>{compare&&<div style={{display:"flex",gap:6,alignItems:"center",marginBottom:7,padding:"6px 9px",background:C.sub,borderRadius:7,border:`1px solid ${C.border}`}}><div style={{flex:1}}><div style={{fontSize:9,color:C.dim,fontWeight:600,marginBottom:1}}>THIS</div><div style={{fontSize:12,fontWeight:700,color:m.color}}>{fv(cur)}</div></div><div style={{width:1,height:24,background:C.border}}/><div style={{flex:1}}><div style={{fontSize:9,color:C.dim,fontWeight:600,marginBottom:1}}>PREV</div><div style={{fontSize:12,fontWeight:700,color:C.muted}}>{fv(prev)}</div></div><div style={{width:1,height:24,background:C.border}}/><div style={{flex:1}}><div style={{fontSize:9,color:C.dim,fontWeight:600,marginBottom:1}}>DIFF</div><div style={{fontSize:12,fontWeight:700,color:up?C.green:"#ef4444"}}>{up?"+":""}{fmt(Math.abs(diff))}</div></div></div>}<CompareChart curData={d.cur} prevData={d.prev} dataKey={m.key} color={m.color} chartType={chartType} compare={compare}/></div>);}
function StatusCard({meta,count,items}){const [open,setOpen]=useState(false);return(<div style={{flex:"1 1 0",minWidth:0,background:C.card,border:`1px solid ${meta.color}25`,borderRadius:10,overflow:"hidden"}}><div onClick={()=>setOpen(o=>!o)} style={{padding:"11px 12px",cursor:"pointer",display:"flex",alignItems:"center",gap:8}}><div style={{width:29,height:29,borderRadius:7,background:meta.bg,display:"flex",alignItems:"center",justifyContent:"center",fontSize:14,flexShrink:0}}>{meta.icon}</div><div style={{flex:1}}><div style={{fontSize:10,color:C.muted,fontWeight:600,letterSpacing:0.3}}>{meta.key.toUpperCase()}</div><div style={{fontSize:19,fontWeight:800,color:meta.color,lineHeight:1.1}}>{count}</div></div><span style={{fontSize:11,color:C.dim,transform:open?"rotate(180deg)":"rotate(0)",transition:".18s"}}>▾</span></div><div style={{height:3,background:C.border,margin:"0 12px"}}><div style={{height:"100%",width:`${Math.min(count*3,100)}%`,background:meta.color,borderRadius:2}}/></div>{open&&<div style={{padding:"7px 10px 9px",display:"flex",flexDirection:"column",gap:4,maxHeight:120,overflowY:"auto"}}>{items.map((it,i)=><div key={i} style={{fontSize:11,color:C.muted,padding:"3px 7px",background:C.sub,borderRadius:4,display:"flex",alignItems:"center",gap:5}}><span style={{width:4,height:4,borderRadius:"50%",background:meta.color,flexShrink:0}}/>{it}</div>)}</div>}</div>);}

function RobotCharacter({state,size=52}){
  const s=size;
  const colors={idle:{body:"#1e2a3a",head:"#243044",eye:"#6366f1",antenna:"#6366f1",glow:"#6366f140"},listening:{body:"#1a2a1a",head:"#1e3a1e",eye:"#10b981",antenna:"#10b981",glow:"#10b98150"},thinking:{body:"#2a1a2a",head:"#3a1e3a",eye:"#8b5cf6",antenna:"#8b5cf6",glow:"#8b5cf650"},speaking:{body:"#1a1e2a",head:"#1e2440",eye:"#ec4899",antenna:"#ec4899",glow:"#ec489950"}};
  const col=colors[state]||colors.idle;
  return(<div style={{position:"relative",width:s,height:s,display:"flex",alignItems:"center",justifyContent:"center"}}><div style={{position:"absolute",inset:-4,borderRadius:"50%",background:`radial-gradient(circle,${col.glow} 0%,transparent 70%)`,animation:state==="idle"?"robotPulse 3s ease-in-out infinite":"robotPulseActive 1s ease-in-out infinite"}}/><svg width={s} height={s} viewBox="0 0 100 100" style={{filter:`drop-shadow(0 0 6px ${col.antenna}80)`}}><rect x="47" y="4" width="6" height="14" rx="3" fill={col.antenna} opacity="0.9"/><circle cx="50" cy="4" r="5" fill={col.antenna}/><rect x="18" y="17" width="64" height="42" rx="12" fill={col.head}/><rect x="22" y="20" width="56" height="6" rx="4" fill="white" opacity="0.07"/><rect x="24" y="27" width="22" height="18" rx="5" fill="#0d1117"/><rect x="54" y="27" width="22" height="18" rx="5" fill="#0d1117"/><rect x="26" y="29" width="18" height="14" rx="4" fill={col.eye} opacity="0.25"/><rect x="56" y="29" width="18" height="14" rx="4" fill={col.eye} opacity="0.25"/><circle cx="35" cy="36" r="5" fill={col.eye}/><circle cx="33" cy="34" r="2" fill="white" opacity="0.6"/><circle cx="65" cy="36" r="5" fill={col.eye}/><circle cx="63" cy="34" r="2" fill="white" opacity="0.6"/>{state==="speaking"?(<>{[0,1,2,3,4].map(i=><rect key={i} x={28+i*9} y="52" width="5" height={3+Math.sin(i)*2} rx="2" fill={col.eye} opacity="0.9"/>)}</>):state==="thinking"?(<><circle cx="35" cy="54" r="2.5" fill={col.eye} opacity="0.7"/><circle cx="50" cy="54" r="2.5" fill={col.eye} opacity="0.5"/><circle cx="65" cy="54" r="2.5" fill={col.eye} opacity="0.3"/></>):(<rect x="30" y="52" width="40" height="5" rx="3" fill={col.eye} opacity={state==="listening"?0.9:0.5}/>)}<rect x="26" y="60" width="48" height="30" rx="8" fill={col.body}/><rect x="34" y="67" width="32" height="16" rx="4" fill="#0d1117" opacity="0.8"/><circle cx="42" cy="75" r="3" fill={col.eye} opacity={state!=="idle"?0.9:0.4}/><circle cx="50" cy="75" r="3" fill={col.antenna} opacity={state==="thinking"||state==="speaking"?0.9:0.3}/><circle cx="58" cy="75" r="3" fill={C.green} opacity={state==="listening"?0.9:0.3}/><rect x="12" y="62" width="12" height="22" rx="6" fill={col.body}/><rect x="76" y="62" width="12" height="22" rx="6" fill={col.body}/><rect x="32" y="90" width="14" height="10" rx="4" fill={col.body}/><rect x="54" y="90" width="14" height="10" rx="4" fill={col.body}/></svg></div>);
}

function FloatingAgent({onCommand}){
  const [open,setOpen]=useState(false);
  const [msgs,setMsgs]=useState([{role:"assistant",content:"မင်္ဂလာပါ Sayar Gyi! 👋\n\nChat လည်းရ၊ Voice နဲ့လည်းခိုင်းလို့ရပါတယ်။\n\n🎙 ဥပမာ:\n• \"Dashboard ကိုပြပါ\"\n• \"TikTok data ကြည့်ချင်တယ်\"\n• \"Fashion Brand client ကိုဖွင့်\"\n• \"Brand DNA ကိုသွားပါ\""}]);
  const [input,setInput]=useState("");const [loading,setLoading]=useState(false);const [robState,setRobState]=useState("idle");const [listening,setListening]=useState(false);const [voiceSupported]=useState(()=>!!(window.SpeechRecognition||window.webkitSpeechRecognition));const msgEnd=useRef(null);const recognRef=useRef(null);
  useEffect(()=>{if(msgEnd.current)msgEnd.current.scrollIntoView({behavior:"smooth"});},[msgs,loading]);
  const parseCommand=useCallback((text)=>{const t=text.toLowerCase();const navMap=[{patterns:["dashboard","main"],action:()=>onCommand({type:"navigate",page:"dashboard"})},{patterns:["news","trend","သတင်း"],action:()=>onCommand({type:"navigate",page:"news"})},{patterns:["brand","brand dna"],action:()=>onCommand({type:"navigate",page:"brand"})},{patterns:["content"],action:()=>onCommand({type:"navigate",page:"content"})},{patterns:["archive","project"],action:()=>onCommand({type:"navigate",page:"archive"})},{patterns:["assets"],action:()=>onCommand({type:"navigate",page:"assets"})},{patterns:["creator"],action:()=>onCommand({type:"navigate",page:"creator"})},{patterns:["status"],action:()=>onCommand({type:"navigate",page:"status"})},{patterns:["facebook","fb"],action:()=>onCommand({type:"platform",value:"Facebook"})},{patterns:["tiktok"],action:()=>onCommand({type:"platform",value:"TikTok"})},{patterns:["youtube","yt"],action:()=>onCommand({type:"platform",value:"YouTube"})},{patterns:["real estate"],action:()=>onCommand({type:"client",value:"Real Estate Co."})},{patterns:["fashion"],action:()=>onCommand({type:"client",value:"Fashion Brand"})},{patterns:["restaurant"],action:()=>onCommand({type:"client",value:"Restaurant Chain"})},{patterns:["tech"],action:()=>onCommand({type:"client",value:"Tech Startup"})},{patterns:["beauty"],action:()=>onCommand({type:"client",value:"Beauty Studio"})},{patterns:["all clients","all"],action:()=>onCommand({type:"client",value:"All Clients"})},{patterns:["weekly"],action:()=>onCommand({type:"timeframe",value:"Weekly"})},{patterns:["monthly"],action:()=>onCommand({type:"timeframe",value:"Monthly"})},{patterns:["yearly"],action:()=>onCommand({type:"timeframe",value:"Yearly"})}];for(const {patterns,action} of navMap){if(patterns.some(p=>t.includes(p))){action();return true;}}return false;},[onCommand]);
  const send=async(text)=>{const t=(text||input).trim();if(!t||loading)return;setInput("");const userMsg={role:"user",content:t};const history=[...msgs,userMsg];setMsgs(history);setLoading(true);setRobState("thinking");const handled=parseCommand(t);try{const res=await fetch("https://api.anthropic.com/v1/messages",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({model:"claude-sonnet-4-20250514",max_tokens:800,system:`You are a smart AI Agent inside "Sayar Gyi's AI Command Center" — an AI Marketing Agency dashboard for the Myanmar market. Help CEO Sayar Gyi with marketing strategy, content ideas, performance analysis, and navigation. Reply concisely. Support Myanmar + English naturally. If user asked to navigate/open something, confirm you've done it${handled?" (action triggered)":""}.`,messages:history.map(m=>({role:m.role,content:m.content}))})});const data=await res.json();const reply=data.content?.map(b=>b.text||"").join("")||"⚠️ No response.";setMsgs(prev=>[...prev,{role:"assistant",content:reply}]);setRobState("speaking");setTimeout(()=>setRobState("idle"),2500);}catch(e){setMsgs(prev=>[...prev,{role:"assistant",content:"⚠️ Connection error."}]);setRobState("idle");}setLoading(false);};
  const toggleVoice=()=>{if(!voiceSupported)return;if(listening){recognRef.current?.stop();setListening(false);setRobState("idle");return;}const SR=window.SpeechRecognition||window.webkitSpeechRecognition;const r=new SR();r.continuous=false;r.interimResults=false;r.lang="en-US";r.onstart=()=>{setListening(true);setRobState("listening");};r.onresult=e=>{const tr=e.results[0][0].transcript;setListening(false);send(tr);};r.onerror=()=>{setListening(false);setRobState("idle");};r.onend=()=>setListening(false);recognRef.current=r;r.start();};
  return(<><style>{`@keyframes robotFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-5px)}}@keyframes robotPulse{0%,100%{opacity:0.4;transform:scale(1)}50%{opacity:0.7;transform:scale(1.05)}}@keyframes robotPulseActive{0%,100%{opacity:0.6;transform:scale(1)}50%{opacity:1;transform:scale(1.12)}}@keyframes bounce{0%,80%,100%{transform:scaleY(0.4)}40%{transform:scaleY(1)}}@keyframes slideUp{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}@keyframes spin{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}`}</style>{open&&(<div style={{position:"fixed",bottom:82,right:20,width:340,height:500,background:"#080e1a",border:`1px solid #1e2d45`,borderRadius:18,display:"flex",flexDirection:"column",zIndex:1000,boxShadow:"0 24px 64px #00000099",overflow:"hidden",animation:"slideUp .2s ease"}}><div style={{padding:"12px 14px 10px",background:"#0a1220",borderBottom:`1px solid #1e2d45`,display:"flex",alignItems:"center",gap:10,flexShrink:0}}><div style={{animation:"robotFloat 3s ease-in-out infinite",flexShrink:0}}><RobotCharacter state={robState} size={40}/></div><div style={{flex:1}}><div style={{fontSize:13,fontWeight:800,color:C.head}}>AI Command Agent</div><div style={{display:"flex",alignItems:"center",gap:5,marginTop:2}}><span style={{width:5,height:5,borderRadius:"50%",background:listening?C.green:C.fb}}/><span style={{fontSize:10,color:listening?C.green:C.muted,fontWeight:600}}>{listening?"Listening...":loading?"Processing...":robState==="speaking"?"Speaking...":"Ready"}</span></div></div><div style={{display:"flex",gap:5}}>{voiceSupported&&<button onClick={toggleVoice} style={{width:28,height:28,borderRadius:7,border:`1px solid ${listening?"#ef4444":C.border}`,background:listening?"#ef444420":"#1a2235",color:listening?"#ef4444":C.muted,cursor:"pointer",fontSize:12,display:"flex",alignItems:"center",justifyContent:"center"}}>{listening?"⏹":"🎤"}</button>}<button onClick={()=>setOpen(false)} style={{width:28,height:28,borderRadius:7,border:`1px solid ${C.border}`,background:"transparent",color:C.dim,cursor:"pointer",fontSize:12,display:"flex",alignItems:"center",justifyContent:"center"}}>✕</button></div></div><div style={{padding:"7px 10px",background:"#0a1220",borderBottom:`1px solid #1a2535`,display:"flex",gap:4,overflowX:"auto",flexShrink:0}}>{["📊 Dashboard","🧬 Brand DNA","📡 News","🎬 Creator","📈 Facebook","🎵 TikTok"].map(cmd=>(<button key={cmd} onClick={()=>send(cmd.split(" ").slice(1).join(" "))} style={{padding:"3px 8px",borderRadius:99,border:`1px solid #1e2d45`,background:"#111827",color:C.muted,fontSize:10,fontWeight:600,cursor:"pointer",whiteSpace:"nowrap",flexShrink:0}}>{cmd}</button>))}</div><div style={{flex:1,overflowY:"auto",padding:"10px 10px 4px",display:"flex",flexDirection:"column",gap:8}}>{msgs.map((m,i)=>(<div key={i} style={{display:"flex",alignItems:"flex-end",gap:6,flexDirection:m.role==="user"?"row-reverse":"row"}}>{m.role==="assistant"&&<div style={{flexShrink:0}}><RobotCharacter state="idle" size={22}/></div>}<div style={{maxWidth:"80%",padding:"8px 11px",borderRadius:m.role==="user"?"14px 14px 3px 14px":"14px 14px 14px 3px",background:m.role==="user"?"linear-gradient(135deg,#4f46e5,#7c3aed)":"#111e30",color:C.text,fontSize:11,lineHeight:1.6,wordBreak:"break-word"}}>{m.content.split("\n").map((line,li)=><div key={li}>{line||<br/>}</div>)}</div></div>))}{loading&&(<div style={{display:"flex",alignItems:"flex-end",gap:6}}><div style={{flexShrink:0}}><RobotCharacter state="thinking" size={22}/></div><div style={{padding:"10px 13px",borderRadius:"14px 14px 14px 3px",background:"#111e30",display:"flex",gap:4,alignItems:"center",height:34}}>{[0,1,2].map(i=><span key={i} style={{width:6,height:6,borderRadius:"50%",background:"#6366f1",display:"inline-block",animation:`bounce 1.2s ${i*0.2}s infinite`}}/>)}</div></div>)}<div ref={msgEnd}/></div><div style={{padding:"8px 10px 11px",borderTop:`1px solid #1a2535`,background:"#0a1220",display:"flex",gap:6,alignItems:"flex-end",flexShrink:0}}><textarea value={input} onChange={e=>setInput(e.target.value)} onKeyDown={e=>{if(e.key==="Enter"&&!e.shiftKey){e.preventDefault();send();}}} placeholder="ရိုက်ပါ (Enter to send)" rows={1} style={{flex:1,background:"#111e30",border:`1px solid ${C.border}`,borderRadius:9,padding:"7px 10px",color:C.text,fontSize:12,outline:"none",resize:"none",fontFamily:"inherit",lineHeight:1.45,maxHeight:68,overflowY:"auto"}}/>{voiceSupported&&<button onClick={toggleVoice} style={{width:32,height:32,borderRadius:8,border:`1px solid ${listening?"#ef4444":C.border}`,background:listening?"#ef444420":"#111e30",color:listening?"#ef4444":C.muted,cursor:"pointer",fontSize:13,display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0}}>{listening?"⏹":"🎤"}</button>}<button onClick={()=>send()} disabled={loading||!input.trim()} style={{width:32,height:32,borderRadius:8,border:"none",background:input.trim()&&!loading?"linear-gradient(135deg,#6366f1,#8b5cf6)":"#1f2937",color:input.trim()&&!loading?"#fff":C.dim,cursor:input.trim()&&!loading?"pointer":"default",fontSize:14,display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0}}>➤</button></div></div>)}<button onClick={()=>setOpen(o=>!o)} style={{position:"fixed",bottom:20,right:20,width:54,height:54,borderRadius:"50%",background:"transparent",border:"none",cursor:"pointer",zIndex:1000,display:"flex",alignItems:"center",justifyContent:"center",animation:"robotFloat 3s ease-in-out infinite"}}><RobotCharacter state={open?robState:"idle"} size={54}/></button></>);}

function FloatingMusic(){
  const [open,setOpen]=useState(false);const [videoId,setVideoId]=useState("");const [inputUrl,setInputUrl]=useState("");
  const extractId=u=>{const m=u.match(/(?:youtu\.be\/|youtube\.com\/(?:watch\?v=|shorts\/|embed\/))([a-zA-Z0-9_-]{11})/);return m?m[1]:null;};
  const load=()=>{const id=extractId(inputUrl);if(id)setVideoId(id);};
  const examples=[{label:"☁ Lo-fi Beats",url:"https://www.youtube.com/watch?v=jfKfPfyJRdk"},{label:"🎯 Focus Music",url:"https://www.youtube.com/watch?v=5qap5aO4i9A"},{label:"🌊 Chill Vibes",url:"https://www.youtube.com/watch?v=DWcJFNfaw9c"}];
  return(<>{open&&(<div style={{position:"fixed",bottom:82,right:84,width:280,background:"#080e1a",border:`1px solid #1e2d45`,borderRadius:14,overflow:"hidden",zIndex:999,boxShadow:"0 24px 64px #00000099",animation:"slideUp .2s ease"}}><div style={{padding:"10px 13px",background:"#0a1220",borderBottom:`1px solid #1e2d45`,display:"flex",alignItems:"center",gap:7}}><span style={{fontSize:15}}>🎵</span><div style={{flex:1,fontSize:12,fontWeight:700,color:C.head}}>Music Player</div><button onClick={()=>setOpen(false)} style={{background:"none",border:"none",color:C.dim,cursor:"pointer",fontSize:13}}>✕</button></div>{videoId?<iframe key={videoId} src={`https://www.youtube.com/embed/${videoId}?autoplay=1&controls=1`} width="280" height="157" allow="autoplay; encrypted-media" frameBorder="0" style={{display:"block"}}/>:(<div style={{padding:"13px",textAlign:"center"}}><div style={{fontSize:32,marginBottom:5}}>🎧</div><div style={{fontSize:11,color:C.muted,marginBottom:10}}>Paste a YouTube URL to start</div><div style={{display:"flex",flexDirection:"column",gap:4}}>{examples.map(e=><button key={e.label} onClick={()=>{setInputUrl(e.url);const id=extractId(e.url);if(id)setVideoId(id);}} style={{padding:"6px 9px",background:"#111e30",border:`1px solid #1e2d45`,borderRadius:7,color:C.text,fontSize:11,cursor:"pointer",textAlign:"left"}}>{e.label}</button>)}</div></div>)}<div style={{padding:"9px 10px 11px",borderTop:`1px solid #1a2535`,background:"#0a1220",display:"flex",gap:5}}><input value={inputUrl} onChange={e=>setInputUrl(e.target.value)} onKeyDown={e=>e.key==="Enter"&&load()} placeholder="Paste YouTube URL..." style={{flex:1,background:"#111e30",border:`1px solid #1e2d45`,borderRadius:7,padding:"6px 8px",color:C.text,fontSize:11,outline:"none"}}/><button onClick={load} style={{padding:"6px 11px",background:"#6366f1",border:"none",borderRadius:7,color:"#fff",fontSize:11,fontWeight:700,cursor:"pointer"}}>▶</button></div></div>)}<button onClick={()=>setOpen(o=>!o)} style={{position:"fixed",bottom:20,right:84,width:42,height:42,borderRadius:"50%",background:"#111827",border:`1px solid ${open?"#6366f160":C.border}`,cursor:"pointer",display:"flex",alignItems:"center",justifyContent:"center",fontSize:17,zIndex:1000,color:open?C.fb:C.muted}}>🎵</button></>);}

// ── Dashboard Page ─────────────────────────────────────────────────────────────
function DashboardPage({client,voicePlatform,voiceTf}){
  const [sPlatform,setSPlatform]=useState("All");const [sTf,setSTf]=useState("Weekly");const [sCStart,setSCStart]=useState("");const [sCEnd,setSCEnd]=useState("");
  const [platform,setPlatform]=useState("Facebook");const [tf,setTf]=useState("Weekly");const [chartType,setChartType]=useState("Area");const [compare,setCompare]=useState(false);const [cStart,setCStart]=useState("");const [cEnd,setCEnd]=useState("");
  useEffect(()=>{if(voicePlatform)setPlatform(voicePlatform);},[voicePlatform]);useEffect(()=>{if(voiceTf)setTf(voiceTf);},[voiceTf]);
  const clientData=STATUS_DATA[client]||STATUS_DATA["All Clients"];const statusSrc=clientData[sPlatform==="All"?"All":sPlatform]||clientData["All"];const platData=PLATFORMS[platform];const TFS=["Weekly","Monthly","Yearly","Custom"];const tfLabel={Weekly:"vs Last Week",Monthly:"vs Last Month",Yearly:"vs Last Year",Custom:"vs Previous Period"};
  return(<div style={{display:"flex",flexDirection:"column",gap:20}}><section><div style={{display:"flex",alignItems:"center",justifyContent:"space-between",marginBottom:10,flexWrap:"wrap",gap:8}}><div><div style={{fontSize:14,fontWeight:700,color:C.text}}>✍️ Content Creation Status</div><div style={{fontSize:11,color:C.dim,marginTop:1}}>Click any card to expand</div></div><div style={{display:"flex",gap:5}}><SegPicker small options={["All","Facebook","TikTok","YouTube"]} value={sPlatform} onChange={setSPlatform} colorFn={o=>({Facebook:C.fb,TikTok:C.tt,YouTube:C.yt}[o])}/><SegPicker small options={["Weekly","Monthly","Yearly","Custom"]} value={sTf} onChange={setSTf}/></div></div>{sTf==="Custom"&&<div style={{display:"flex",gap:6,alignItems:"center",marginBottom:9,flexWrap:"wrap"}}><input type="date" value={sCStart} onChange={e=>setSCStart(e.target.value)} style={{background:C.sub,border:`1px solid #374151`,borderRadius:5,padding:"4px 8px",color:C.text,fontSize:11,outline:"none"}}/><span style={{fontSize:11,color:C.dim}}>→</span><input type="date" value={sCEnd} onChange={e=>setSCEnd(e.target.value)} style={{background:C.sub,border:`1px solid #374151`,borderRadius:5,padding:"4px 8px",color:C.text,fontSize:11,outline:"none"}}/><button style={{padding:"4px 10px",background:C.fb,border:"none",borderRadius:5,color:"#fff",fontSize:11,fontWeight:700,cursor:"pointer"}}>Apply</button></div>}<div style={{display:"grid",gridTemplateColumns:"repeat(4,1fr)",gap:9}}>{STATUS_META.map(meta=>{const d=statusSrc[meta.key]||{count:0,items:[]};return <StatusCard key={meta.key} meta={meta} count={d.count} items={d.items}/>;})}</div><div style={{marginTop:7,background:C.card,border:`1px solid ${C.border}`,borderRadius:7,padding:"7px 12px",display:"flex",alignItems:"center",gap:5,flexWrap:"wrap"}}>{STATUS_META.map((d,i)=>{const cnt=(statusSrc[d.key]||{}).count||0;return(<div key={d.key} style={{display:"flex",alignItems:"center",gap:3}}><span style={{fontSize:10,color:d.color,fontWeight:700}}>{d.key}</span><span style={{fontSize:10,background:d.bg,color:d.color,padding:"1px 6px",borderRadius:99,fontWeight:700}}>{cnt}</span>{i<STATUS_META.length-1&&<span style={{color:C.dim,fontSize:10,margin:"0 2px"}}>→</span>}</div>);})}<div style={{marginLeft:"auto",fontSize:10,color:C.dim}}>{sPlatform==="All"?"All Platforms":sPlatform} · {sTf}</div></div></section><section><div style={{display:"flex",alignItems:"center",justifyContent:"space-between",marginBottom:10,flexWrap:"wrap",gap:8}}><div><div style={{fontSize:14,fontWeight:700,color:C.text}}>📈 Platform Performance</div><div style={{fontSize:11,color:C.dim,marginTop:1}}><span style={{color:platData.color,fontWeight:700}}>{platform}</span> · {tf}{compare&&<span style={{color:C.amber,fontWeight:600}}> · {tfLabel[tf]}</span>}</div></div><div style={{display:"flex",gap:5,flexWrap:"wrap",alignItems:"center"}}><SegPicker small options={["Facebook","TikTok","YouTube"]} value={platform} onChange={setPlatform} colorFn={o=>({Facebook:C.fb,TikTok:C.tt,YouTube:C.yt}[o])}/><SegPicker small options={["Area","Line","Bar"]} value={chartType} onChange={setChartType}/><SegPicker small options={TFS} value={tf} onChange={setTf}/><button onClick={()=>setCompare(o=>!o)} style={{padding:"2px 8px",borderRadius:5,border:`1px solid ${compare?C.amber+"80":C.border}`,background:compare?"#f59e0b14":"transparent",color:compare?C.amber:C.dim,fontSize:10,fontWeight:compare?700:500,cursor:"pointer"}}>⇄ Compare</button></div></div>{tf==="Custom"&&<div style={{display:"flex",gap:6,alignItems:"center",marginBottom:10,padding:"9px 12px",background:C.card,border:`1px solid ${C.border}`,borderRadius:8,flexWrap:"wrap"}}><span style={{fontSize:11,color:C.muted,fontWeight:600}}>From</span><input type="date" value={cStart} onChange={e=>setCStart(e.target.value)} style={{background:C.sub,border:`1px solid #374151`,borderRadius:5,padding:"4px 8px",color:C.text,fontSize:11,outline:"none"}}/><span style={{fontSize:11,color:C.dim}}>→</span><input type="date" value={cEnd} onChange={e=>setCEnd(e.target.value)} style={{background:C.sub,border:`1px solid #374151`,borderRadius:5,padding:"4px 8px",color:C.text,fontSize:11,outline:"none"}}/><button style={{padding:"4px 11px",background:platData.color,border:"none",borderRadius:5,color:"#fff",fontSize:11,fontWeight:700,cursor:"pointer",marginLeft:4}}>Apply</button></div>}{compare&&<div style={{display:"flex",alignItems:"center",gap:8,marginBottom:10,padding:"7px 12px",background:"#f59e0b08",border:`1px solid #f59e0b25`,borderRadius:8}}><span style={{fontSize:11,color:C.amber,fontWeight:600}}>⇄ {tfLabel[tf]}</span><div style={{marginLeft:"auto",display:"flex",gap:10}}><div style={{display:"flex",alignItems:"center",gap:4}}><div style={{width:14,height:2,background:platData.color,borderRadius:1}}/><span style={{fontSize:10,color:C.dim}}>Current</span></div><div style={{display:"flex",alignItems:"center",gap:4}}><div style={{width:14,height:0,borderTop:`2px dashed ${platData.color}70`}}/><span style={{fontSize:10,color:C.dim}}>Previous</span></div></div></div>}<div style={{display:"flex",flexDirection:"column",gap:9}}>{platData.metrics.map((row,ri)=>(<div key={ri} style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:9}}>{row.map(m=><MetricCard key={m.key} m={m} tf={tf} chartType={chartType} compare={compare}/>)}</div>))}</div></section></div>);}

// ── News Page ──────────────────────────────────────────────────────────────────
function NewsPage(){const [tab,setTab]=useState("Global News");return(<div><h1 style={{fontSize:20,fontWeight:700,color:C.head,margin:"0 0 5px"}}>📡 Industry News & Trend Analysis</h1><p style={{color:C.muted,fontSize:13,margin:"0 0 13px"}}>Real-time AI & Marketing intelligence.</p><div style={{display:"flex",gap:3,marginBottom:13,background:C.card,padding:4,borderRadius:9,width:"fit-content",flexWrap:"wrap"}}>{NEWS_TABS.map(t=><button key={t} onClick={()=>setTab(t)} style={{padding:"6px 12px",borderRadius:6,border:"none",cursor:"pointer",fontSize:12,fontWeight:600,background:tab===t?"#6366f1":"transparent",color:tab===t?"#fff":C.muted}}>{t}</button>)}</div><div style={{display:"flex",flexDirection:"column",gap:8}}>{(NEWS[tab]||[]).map((item,i)=>(<div key={i} style={{background:C.card,border:`1px solid ${C.border}`,borderRadius:9,padding:"11px 13px"}}><div style={{display:"flex",justifyContent:"space-between",marginBottom:5}}><span style={{background:(TAG_C[item.tag]||C.muted)+"22",color:TAG_C[item.tag]||C.muted,fontSize:10,padding:"2px 8px",borderRadius:99,fontWeight:700}}>{item.tag}</span><span style={{fontSize:10,color:C.dim}}>{item.time}</span></div><p style={{margin:"0 0 5px",fontSize:13,color:C.text,fontWeight:500,lineHeight:1.5}}>{item.title}</p><span style={{fontSize:10,color:C.dim}}>Source: {item.src}</span></div>))}</div></div>);}

// ══════════════════════════════════════════════════════════════════════════════
// 🧬 BRAND DNA PAGE — UPGRADED (Manual + AI Generate)
// ══════════════════════════════════════════════════════════════════════════════
const EMPTY_BRAND={name:"",industry:"",audience:"",usp:"",mission:"",promise:"",tagline:"",elevator:"",tone:"",archetype:"",fbTone:"",tiktokTone:"",ytTone:"",dos:"",donts:"",pillars:["","",""],painPoints:"",topicIdeas:"",logoDesc:"",moodboard:"",colors:["#6366f1","#ec4899","#10b981","#f59e0b"],font:"Modern Sans",competitors:[]};
const SAMPLE_BRANDS={"Real Estate Co.":{name:"Real Estate Co.",industry:"Real Estate & Property",audience:"Home buyers 28-50, urban professionals in Yangon",usp:"Trusted property solutions with AI-powered market insights",mission:"Helping families find their dream home with confidence",promise:"Full transparency in every property transaction — guaranteed",tagline:"Your Trusted Home, Our Trusted Guidance",elevator:"We help Yangon families find verified properties with zero stress using AI-powered matching and transparent pricing.",tone:"Professional",archetype:"Sage",fbTone:"Informative and data-driven with market highlights",tiktokTone:"Short property tour clips with surprising price reveals",ytTone:"In-depth area guides and investment explainers",dos:"Use data, cite sources, share client testimonials, stay formal",donts:"No slang, no unverified claims, no emotional oversell",pillars:["Market Insights & Trends","Property Investment Tips","Client Success Stories"],painPoints:"Buyers fear fraud, unclear pricing, and finding trustworthy agents",topicIdeas:"Property price comparisons, neighborhood guides, buyer mistake series, investment ROI breakdowns",logoDesc:"Clean geometric house icon with modern sans-serif wordmark in navy blue",moodboard:"trustworthy, modern, clean, premium, urban",colors:["#1e40af","#0ea5e9","#f8fafc","#1e293b"],font:"Modern Sans",competitors:[{name:"Property Guru",note:"Strong SEO, weak social"},{name:"iProperty",note:"Good listings, no content strategy"}]},"Fashion Brand":{name:"Fashion Brand",industry:"Fashion & Lifestyle",audience:"Trendy women 18-35, style-conscious millennials Myanmar",usp:"Affordable luxury streetwear celebrating SEA identity",mission:"Making fashion a form of self-expression for every woman",promise:"You'll always turn heads — or your money back",tagline:"Wear Bold. Be You.",elevator:"Fashion Brand makes premium streetwear affordable for Myanmar's bold generation — where your outfit tells your story.",tone:"Trendy",archetype:"Creator",fbTone:"Aspirational lifestyle posts with strong visual hooks",tiktokTone:"Viral try-on hauls, GRWM, trending sounds",ytTone:"Mini fashion documentaries and style transformation videos",dos:"Use vivid visuals, trending audio, bold CTAs, influencer collabs",donts:"No boring flat lays, no formal language, no outdated aesthetics",pillars:["New Arrivals & Lookbooks","Style Tips & Outfit Ideas","Behind the Brand Stories"],painPoints:"Can't afford luxury brands, local fashion feels outdated, no style identity",topicIdeas:"Get the look for less, Myanmar street style features, behind-the-design stories, seasonal trend forecasts",logoDesc:"Abstract letter mark with bold italic font, hot pink gradient",moodboard:"bold, edgy, colorful, rebellious, youthful, maximalist",colors:["#ec4899","#f472b6","#fdf2f8","#1a1a2e"],font:"Display Serif",competitors:[{name:"Pomelo Fashion",note:"Strong IG, high price point"},{name:"Zara SEA",note:"Big brand, no local relevance"}]},"Restaurant Chain":{name:"Restaurant Chain",industry:"F&B / Restaurant",audience:"Food lovers 22-45, families & couples in Myanmar",usp:"Authentic Myanmar flavors reimagined for modern dining",mission:"Bringing communities together through the joy of shared meals",promise:"Every visit feels like dining at grandma's — with a modern twist",tagline:"Where Every Meal Tells a Story",elevator:"We serve Myanmar's favorite flavors in a warm, modern setting that makes every meal feel like a family reunion.",tone:"Friendly",archetype:"Everyman",fbTone:"Warm, storytelling-driven, feature customer moments",tiktokTone:"Food reveal videos, chef's secret recipes, ASMR cooking",ytTone:"Full recipe tutorials and restaurant tour vlogs",dos:"Show real food, feature staff, use warm colors, share recipes",donts:"No corporate language, no stock photos, no empty promises",pillars:["Food Stories & Heritage","New Menu Highlights","Customer Moments & UGC"],painPoints:"Missing authentic taste in modern restaurants, overpriced foreign food",topicIdeas:"Dish origin stories, chef behind the scenes, customer 'first bite' reactions, recipe reveals",logoDesc:"Friendly bowl icon with hand-lettered script font in warm amber",moodboard:"warm, homey, authentic, appetizing, community-driven",colors:["#d97706","#fbbf24","#fff7ed","#1c1917"],font:"Rounded",competitors:[{name:"Local Chains",note:"Traditional menu, zero digital presence"},{name:"KFC Myanmar",note:"Strong brand but not authentic"}]},"Tech Startup":{name:"Tech Startup",industry:"Technology / SaaS",audience:"SME owners 25-45, entrepreneurs Myanmar & SEA",usp:"AI-powered business tools that save 10+ hours per week",mission:"Democratizing powerful technology for every business owner",promise:"Save time in 30 days or full refund",tagline:"Work Smarter. Grow Faster.",elevator:"We build simple AI tools that give Myanmar SMEs the same edge as Fortune 500 companies — at a fraction of the cost.",tone:"Authoritative",archetype:"Magician",fbTone:"Educational with clear ROI stats and before/after results",tiktokTone:"30-second productivity hacks and tool demos",ytTone:"Deep-dive tutorials and founder story documentaries",dos:"Lead with ROI data, use case studies, explain simply",donts:"No heavy jargon, no vague promises, no feature-dumping",pillars:["Productivity & Automation Tips","Customer Case Studies","Industry AI Trends"],painPoints:"SMEs waste hours on manual tasks, can't afford enterprise software",topicIdeas:"AI tool demos, time-saved testimonials, small business automation tips, ROI calculators",logoDesc:"Abstract circuit/brain hybrid icon with bold modern sans-serif in electric indigo",moodboard:"cutting-edge, clean, intelligent, minimal, futuristic",colors:["#6366f1","#8b5cf6","#f5f3ff","#0f172a"],font:"Modern Sans",competitors:[{name:"Local Dev Agencies",note:"Slow, expensive, no AI"},{name:"Freelancers",note:"Cheap but inconsistent"}]},"Beauty Studio":{name:"Beauty Studio",industry:"Beauty & Wellness",audience:"Women 20-40, beauty enthusiasts Myanmar",usp:"Personalized treatments with premium Korean skincare",mission:"Enhancing every woman's natural beauty with science and care",promise:"You'll leave glowing — or your next treatment is free",tagline:"Your Glow, Perfected.",elevator:"We combine Korean beauty science with personalized care to give every Myanmar woman the skin she deserves.",tone:"Elegant",archetype:"Lover",fbTone:"Educational skincare tips with elegant visuals and gentle CTAs",tiktokTone:"Satisfying treatment videos, product reviews, glow-up reveals",ytTone:"Full skincare routine guides and ingredient deep-dives",dos:"Show real results, soft aesthetics, educate on ingredients",donts:"No harsh lighting, no fake before/afters, no aggressive sales",pillars:["Skincare Education & Tips","Before & After Transformations","Product Spotlights"],painPoints:"Generic treatments that don't suit Asian skin, overpriced imports",topicIdeas:"Ingredient explainers, skin type quizzes, seasonal skincare routines, client transformation stories",logoDesc:"Delicate floral monogram with thin serif font in blush and deep rose",moodboard:"feminine, luxurious, soft, glowing, serene, premium, pastel",colors:["#f9a8d4","#fbcfe8","#fdf2f8","#4a0e2e"],font:"Display Serif",competitors:[{name:"Local Salons",note:"No branding, no content strategy"},{name:"Beauty chains",note:"Standardized, not personalized"}]}};

const TONE_OPTIONS=[{key:"Professional",desc:"Trustworthy, formal, expert",icon:"💼",color:"#6366f1"},{key:"Friendly",desc:"Warm, approachable, casual",icon:"😊",color:"#10b981"},{key:"Trendy",desc:"Bold, modern, youth-focused",icon:"🔥",color:"#ec4899"},{key:"Authoritative",desc:"Confident, data-driven, leader",icon:"📊",color:"#3b82f6"},{key:"Elegant",desc:"Refined, premium, sophisticated",icon:"✨",color:"#8b5cf6"},{key:"Playful",desc:"Fun, creative, energetic",icon:"🎨",color:"#f59e0b"}];
const ARCHETYPE_OPTIONS=[{key:"Hero",icon:"⚔️",color:"#ef4444"},{key:"Creator",icon:"🎨",color:"#8b5cf6"},{key:"Sage",icon:"🦉",color:"#3b82f6"},{key:"Jester",icon:"🎭",color:"#f59e0b"},{key:"Caregiver",icon:"💚",color:"#10b981"},{key:"Explorer",icon:"🧭",color:"#14b8a6"},{key:"Ruler",icon:"👑",color:"#6366f1"},{key:"Lover",icon:"❤️",color:"#ec4899"},{key:"Innocent",icon:"🌸",color:"#a3e635"},{key:"Everyman",icon:"🤝",color:"#64748b"},{key:"Outlaw",icon:"🔥",color:"#f97316"},{key:"Magician",icon:"✨",color:"#a855f7"}];
const FONT_OPTIONS=["Modern Sans","Display Serif","Rounded","Monospace","Handwritten"];
const PRESET_COLORS=["#6366f1","#ec4899","#ef4444","#f59e0b","#10b981","#3b82f6","#8b5cf6","#14b8a6","#f472b6","#0ea5e9","#1e40af","#d97706","#065f46","#1e293b","#f8fafc","#ffffff"];

const BRAND_TABS=[{key:"core",label:"Brand Core",icon:"📋"},{key:"voice",label:"Voice & Tone",icon:"🎙"},{key:"content",label:"Content Strategy",icon:"🏛"},{key:"visual",label:"Visual ID",icon:"🎨"},{key:"competitors",label:"Competitors",icon:"🏆"}];

function FieldInput({label,required,value,onChange,placeholder,multiline,rows=2}){
  const base={width:"100%",background:"#0d1117",border:`1px solid ${value?C.fb+"60":C.border}`,borderRadius:8,padding:"9px 12px",color:C.text,fontSize:13,outline:"none",fontFamily:"inherit",boxSizing:"border-box",transition:"border .15s"};
  return(<div><label style={{fontSize:10,color:"#9ca3af",fontWeight:600,display:"flex",alignItems:"center",gap:5,marginBottom:5,letterSpacing:0.5}}>{label.toUpperCase()}{required&&<span style={{color:C.fb,fontSize:9}}>● REQUIRED</span>}</label>{multiline?<textarea value={value} onChange={e=>onChange(e.target.value)} placeholder={placeholder} rows={rows} style={{...base,resize:"vertical"}}/>:<input value={value} onChange={e=>onChange(e.target.value)} placeholder={placeholder} style={base}/>}</div>);
}

// AI Generate Flow
function AIGenerateMode({onApply,client}){
  const [step,setStep]=useState(1); // 1=form, 2=generating, 3=preview
  const [brief,setBrief]=useState({name:client!=="All Clients"?client:"",industry:"",audience:"",description:"",platforms:"Facebook, TikTok, YouTube"});
  const [generated,setGenerated]=useState(null);
  const [err,setErr]=useState("");

  const generate=async()=>{
    if(!brief.name||!brief.industry){setErr("Brand Name နှင့် Industry ဖြည့်ပေးပါ");return;}
    setErr("");setStep(2);
    try{
      const prompt=`You are an expert brand strategist for Myanmar's digital marketing market. Generate a complete Brand DNA in JSON format for this business:

Brand Name: ${brief.name}
Industry: ${brief.industry}
Target Audience: ${brief.audience||"Not specified"}
Brief Description: ${brief.description||"Not specified"}
Platforms: ${brief.platforms}

Return ONLY a valid JSON object (no markdown, no backticks) with these exact keys:
{
  "name": "",
  "industry": "",
  "audience": "",
  "usp": "",
  "mission": "",
  "promise": "",
  "tagline": "",
  "elevator": "",
  "tone": "(one of: Professional/Friendly/Trendy/Authoritative/Elegant/Playful)",
  "archetype": "(one of: Hero/Creator/Sage/Jester/Caregiver/Explorer/Ruler/Lover/Innocent/Everyman/Outlaw/Magician)",
  "fbTone": "",
  "tiktokTone": "",
  "ytTone": "",
  "dos": "",
  "donts": "",
  "pillars": ["","",""],
  "painPoints": "",
  "topicIdeas": "",
  "logoDesc": "",
  "moodboard": "",
  "colors": ["#hex1","#hex2","#hex3","#hex4"],
  "font": "(one of: Modern Sans/Display Serif/Rounded/Monospace/Handwritten)",
  "competitors": [{"name":"","note":""},{"name":"","note":""}]
}

Write all content in English. Make it specific, professional, and tailored for Myanmar market. Be creative and insightful.`;
      const res=await fetch("https://api.anthropic.com/v1/messages",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({model:"claude-sonnet-4-20250514",max_tokens:2000,messages:[{role:"user",content:prompt}]})});
      const data=await res.json();
      const raw=data.content?.map(b=>b.text||"").join("")||"";
      const clean=raw.replace(/```json|```/g,"").trim();
      const parsed=JSON.parse(clean);
      // ensure arrays
      if(!Array.isArray(parsed.pillars))parsed.pillars=["","",""];
      if(!Array.isArray(parsed.colors))parsed.colors=["#6366f1","#ec4899","#10b981","#f59e0b"];
      if(!Array.isArray(parsed.competitors))parsed.competitors=[];
      setGenerated(parsed);setStep(3);
    }catch(e){setErr("AI generation failed. Please try again.");setStep(1);}
  };

  if(step===2)return(
    <div style={{display:"flex",flexDirection:"column",alignItems:"center",justifyContent:"center",gap:20,padding:"40px 20px",textAlign:"center"}}>
      <div style={{animation:"robotFloat 2s ease-in-out infinite"}}><RobotCharacter state="thinking" size={72}/></div>
      <div><div style={{fontSize:16,fontWeight:700,color:C.head,marginBottom:6}}>AI သည် Brand DNA ထုတ်လုပ်နေသည်...</div><div style={{fontSize:13,color:C.muted}}>Industry data နှင့် Myanmar market ကို analyze လုပ်နေသည်</div></div>
      <div style={{display:"flex",flexDirection:"column",gap:8,width:"100%",maxWidth:300}}>
        {["Brand Positioning ခွဲခြမ်းနေသည်","Target Audience Profiling","Content Strategy ချနေသည်","Visual Identity Generate လုပ်နေသည်"].map((t,i)=>(
          <div key={i} style={{display:"flex",alignItems:"center",gap:8,padding:"8px 12px",background:C.card,borderRadius:8,border:`1px solid ${C.border}`}}>
            <div style={{width:16,height:16,borderRadius:"50%",border:`2px solid ${C.fb}`,borderTopColor:"transparent",animation:"spin 1s linear infinite",flexShrink:0}}/>
            <span style={{fontSize:12,color:C.muted}}>{t}</span>
          </div>
        ))}
      </div>
    </div>
  );

  if(step===3&&generated)return(
    <div style={{display:"flex",flexDirection:"column",gap:14}}>
      <div style={{display:"flex",alignItems:"center",gap:10,padding:"12px 16px",background:"#10b98110",border:"1px solid #10b98130",borderRadius:10}}>
        <span style={{fontSize:22}}>✅</span>
        <div style={{flex:1}}><div style={{fontSize:13,fontWeight:700,color:C.green}}>Brand DNA Successfully Generated!</div><div style={{fontSize:11,color:C.muted,marginTop:2}}>Preview ကြည့်ပြီး Apply လုပ်ပါ သို့မဟုတ် Manual Tab မှာ Edit ဆက်လုပ်နိုင်ပါသည်</div></div>
      </div>
      {/* Preview cards */}
      <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10}}>
        {[{label:"Brand Name",val:generated.name},{label:"Industry",val:generated.industry},{label:"Tagline",val:generated.tagline},{label:"Tone",val:generated.tone},{label:"Archetype",val:generated.archetype},{label:"Font",val:generated.font}].map(f=>(
          <div key={f.label} style={{background:C.card,border:`1px solid ${C.border}`,borderRadius:8,padding:"10px 12px"}}>
            <div style={{fontSize:9,color:C.dim,fontWeight:600,marginBottom:3}}>{f.label.toUpperCase()}</div>
            <div style={{fontSize:12,color:C.text,fontWeight:600}}>{f.val||"—"}</div>
          </div>
        ))}
      </div>
      <div style={{background:C.card,border:`1px solid ${C.border}`,borderRadius:9,padding:"12px 14px"}}>
        <div style={{fontSize:10,color:C.dim,fontWeight:600,marginBottom:5}}>USP</div>
        <div style={{fontSize:12,color:C.text,lineHeight:1.6}}>{generated.usp}</div>
      </div>
      <div style={{background:C.card,border:`1px solid ${C.border}`,borderRadius:9,padding:"12px 14px"}}>
        <div style={{fontSize:10,color:C.dim,fontWeight:600,marginBottom:5}}>ELEVATOR PITCH</div>
        <div style={{fontSize:12,color:C.text,lineHeight:1.6,fontStyle:"italic"}}>"{generated.elevator}"</div>
      </div>
      <div style={{background:C.card,border:`1px solid ${C.border}`,borderRadius:9,padding:"12px 14px"}}>
        <div style={{fontSize:10,color:C.dim,fontWeight:600,marginBottom:7}}>CONTENT PILLARS</div>
        <div style={{display:"flex",flexDirection:"column",gap:5}}>
          {(generated.pillars||[]).map((p,i)=><div key={i} style={{display:"flex",alignItems:"center",gap:8,fontSize:12,color:C.text}}><span style={{width:18,height:18,borderRadius:5,background:`${[C.fb,C.tt,C.green][i]}20`,color:[C.fb,C.tt,C.green][i],fontSize:10,fontWeight:700,display:"flex",alignItems:"center",justifyContent:"center"}}>{i+1}</span>{p}</div>)}
        </div>
      </div>
      <div style={{background:C.card,border:`1px solid ${C.border}`,borderRadius:9,padding:"12px 14px"}}>
        <div style={{fontSize:10,color:C.dim,fontWeight:600,marginBottom:7}}>COLOR PALETTE</div>
        <div style={{display:"flex",gap:8}}>{(generated.colors||[]).map((c,i)=><div key={i} style={{textAlign:"center"}}><div style={{width:36,height:36,borderRadius:8,background:c,border:`1px solid ${C.border}`}}/><div style={{fontSize:9,color:C.dim,marginTop:3,fontFamily:"monospace"}}>{c}</div></div>)}</div>
      </div>
      <div style={{display:"flex",gap:9}}>
        <button onClick={()=>setStep(1)} style={{flex:1,padding:"10px",background:"transparent",border:`1px solid ${C.border}`,borderRadius:9,color:C.muted,fontSize:13,fontWeight:600,cursor:"pointer"}}>↩ Regenerate</button>
        <button onClick={()=>onApply(generated)} style={{flex:2,padding:"10px",background:"linear-gradient(135deg,#6366f1,#8b5cf6)",border:"none",borderRadius:9,color:"#fff",fontSize:13,fontWeight:700,cursor:"pointer"}}>✨ Apply to Brand DNA</button>
      </div>
    </div>
  );

  // Step 1 — Brief Form
  return(
    <div style={{display:"flex",flexDirection:"column",gap:16}}>
      <div style={{padding:"14px 16px",background:"linear-gradient(135deg,#6366f110,#8b5cf610)",border:"1px solid #6366f130",borderRadius:12}}>
        <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:6}}>
          <span style={{fontSize:22}}>🤖</span>
          <div><div style={{fontSize:13,fontWeight:700,color:C.head}}>AI Brand DNA Generator</div><div style={{fontSize:11,color:C.muted}}>Basic info ၄ ခုသာ ဖြည့်ပါ — AI က Brand DNA အပြည့်အစုံ ထုတ်ပေးမည်</div></div>
        </div>
        <div style={{display:"flex",gap:6,flexWrap:"wrap"}}>
          {["USP","Mission","Tagline","Tone","Archetype","Content Pillars","Platform Tones","Competitors"].map(t=><span key={t} style={{fontSize:10,padding:"2px 8px",borderRadius:99,background:"#6366f120",color:"#818cf8",fontWeight:600}}>{t}</span>)}
        </div>
      </div>
      <FieldInput label="Brand Name" required value={brief.name} onChange={v=>setBrief(b=>({...b,name:v}))} placeholder="e.g. ဆရာကြီး Coffee Shop"/>
      <FieldInput label="Industry / Niche" required value={brief.industry} onChange={v=>setBrief(b=>({...b,industry:v}))} placeholder="e.g. F&B / Coffee & Beverages"/>
      <FieldInput label="Target Audience (Optional)" value={brief.audience} onChange={v=>setBrief(b=>({...b,audience:v}))} placeholder="e.g. Young professionals 22-35 in Yangon"/>
      <FieldInput label="Brief Description (Optional — More = Better Result)" value={brief.description} onChange={v=>setBrief(b=>({...b,description:v}))} placeholder="e.g. We are a specialty coffee brand that sources beans from Shan State and serves Yangon's creative community..." multiline rows={3}/>
      <div><label style={{fontSize:10,color:"#9ca3af",fontWeight:600,display:"block",marginBottom:6,letterSpacing:0.5}}>TARGET PLATFORMS</label><div style={{display:"flex",gap:6}}>{["Facebook","TikTok","YouTube"].map(p=>{const on=brief.platforms.includes(p);return(<button key={p} onClick={()=>setBrief(b=>({...b,platforms:on?b.platforms.replace(p,"").replace(",,",",").replace(/^,|,$/g,""):b.platforms?b.platforms+", "+p:p}))} style={{padding:"6px 12px",borderRadius:7,border:`1px solid ${on?({Facebook:C.fb,TikTok:C.tt,YouTube:C.yt}[p])+"60":C.border}`,background:on?({Facebook:C.fb,TikTok:C.tt,YouTube:C.yt}[p])+"15":"transparent",color:on?({Facebook:C.fb,TikTok:C.tt,YouTube:C.yt}[p]):C.muted,fontSize:12,fontWeight:on?700:400,cursor:"pointer"}}>{p}</button>);})}</div></div>
      {err&&<div style={{padding:"8px 12px",background:"#ef444415",border:"1px solid #ef444440",borderRadius:7,fontSize:12,color:"#f87171"}}>{err}</div>}
      <button onClick={generate} style={{padding:"12px",background:"linear-gradient(135deg,#6366f1,#8b5cf6)",border:"none",borderRadius:10,color:"#fff",fontSize:14,fontWeight:700,cursor:"pointer",display:"flex",alignItems:"center",justifyContent:"center",gap:8}}>
        <span style={{fontSize:18}}>✨</span> AI နဲ့ Brand DNA Generate လုပ်မည်
      </button>
    </div>
  );
}

// Manual Mode
function ManualMode({form,setF,client}){
  const [tab,setTab]=useState("core");
  const [editColor,setEditColor]=useState(null);
  const [addingComp,setAddingComp]=useState(false);
  const [newComp,setNewComp]=useState({name:"",note:""});
  const s=(k,v)=>setF(f=>({...f,[k]:v}));

  const tonePreview={Professional:`"Our latest market analysis reveals a 34% increase in property demand across Yangon's central district, presenting a strategic opportunity for discerning investors."`,Friendly:`"Hey! 👋 We've got some exciting news — your favorite restaurant just dropped a new menu and trust us, you don't want to miss it!"`,Trendy:`"Drop everything 🔥 This collection just landed and it's giving EVERYTHING. Link in bio before it sells out."`,Authoritative:`"Based on Q1 data, businesses using AI automation reported 3.2x higher output with 40% reduced cost. Numbers speak."`,Elegant:`"Crafted with precision, worn with grace. Our new collection is an ode to timeless femininity."`,Playful:`"Guess what?! 🎉 We just made your Tuesday WAY more interesting! Swipe to see what's cooking 🍳"`};

  return(<>
    <div style={{display:"flex",gap:3,background:C.card,padding:4,borderRadius:10,width:"fit-content",flexWrap:"wrap",marginBottom:16}}>
      {BRAND_TABS.map(t=><button key={t.key} onClick={()=>setTab(t.key)} style={{padding:"6px 12px",borderRadius:7,border:"none",cursor:"pointer",fontSize:11,fontWeight:600,background:tab===t.key?"#6366f1":"transparent",color:tab===t.key?"#fff":C.muted,display:"flex",alignItems:"center",gap:4,whiteSpace:"nowrap"}}><span>{t.icon}</span>{t.label}</button>)}
    </div>

    {/* ── Brand Core ── */}
    {tab==="core"&&<div style={{display:"flex",flexDirection:"column",gap:13}}>
      <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:12}}>
        <FieldInput label="Brand Name" required value={form.name} onChange={v=>s("name",v)} placeholder="e.g. Golden Coffee Myanmar"/>
        <FieldInput label="Industry / Niche" required value={form.industry} onChange={v=>s("industry",v)} placeholder="e.g. F&B / Specialty Coffee"/>
      </div>
      <FieldInput label="Target Audience" required value={form.audience} onChange={v=>s("audience",v)} placeholder="e.g. Young professionals 22-35 in Yangon"/>
      <FieldInput label="Unique Selling Point (USP)" required value={form.usp} onChange={v=>s("usp",v)} placeholder="What makes this brand different from competitors?" multiline rows={2}/>
      <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:12}}>
        <FieldInput label="Brand Mission" value={form.mission} onChange={v=>s("mission",v)} placeholder="Why does this brand exist?" multiline rows={2}/>
        <FieldInput label="Brand Promise" value={form.promise} onChange={v=>s("promise",v)} placeholder="What do you guarantee customers?" multiline rows={2}/>
      </div>
      <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:12}}>
        <FieldInput label="Tagline / Slogan" value={form.tagline} onChange={v=>s("tagline",v)} placeholder="e.g. Work Smarter. Grow Faster."/>
        <FieldInput label="Elevator Pitch" value={form.elevator} onChange={v=>s("elevator",v)} placeholder="Describe brand in 2 sentences..." multiline rows={2}/>
      </div>
    </div>}

    {/* ── Voice & Tone ── */}
    {tab==="voice"&&<div style={{display:"flex",flexDirection:"column",gap:16}}>
      <div><div style={{fontSize:11,color:C.dim,fontWeight:600,marginBottom:10}}>TONE STYLE</div>
        <div style={{display:"grid",gridTemplateColumns:"repeat(3,1fr)",gap:8}}>
          {TONE_OPTIONS.map(t=>{const active=form.tone===t.key;return(<button key={t.key} onClick={()=>s("tone",t.key)} style={{padding:"12px 10px",background:active?t.color+"18":C.card,border:`2px solid ${active?t.color:C.border}`,borderRadius:10,cursor:"pointer",textAlign:"left"}}><div style={{fontSize:20,marginBottom:5}}>{t.icon}</div><div style={{fontSize:12,fontWeight:700,color:active?t.color:C.text,marginBottom:2}}>{t.key}</div><div style={{fontSize:10,color:C.muted,lineHeight:1.4}}>{t.desc}</div>{active&&<div style={{marginTop:6,fontSize:9,color:t.color,fontWeight:700}}>✓ SELECTED</div>}</button>);})}</div>
        {form.tone&&<div style={{marginTop:10,padding:"11px 14px",background:C.card,border:`1px solid ${C.border}`,borderRadius:9}}><div style={{fontSize:10,color:C.dim,fontWeight:600,marginBottom:5}}>TONE PREVIEW</div><div style={{fontSize:12,color:C.text,lineHeight:1.6,fontStyle:"italic"}}>{tonePreview[form.tone]}</div></div>}
      </div>
      <div><div style={{fontSize:11,color:C.dim,fontWeight:600,marginBottom:10}}>BRAND ARCHETYPE</div>
        <div style={{display:"grid",gridTemplateColumns:"repeat(4,1fr)",gap:7}}>
          {ARCHETYPE_OPTIONS.map(a=>{const active=form.archetype===a.key;return(<button key={a.key} onClick={()=>s("archetype",a.key)} style={{padding:"9px 8px",background:active?a.color+"18":C.card,border:`2px solid ${active?a.color:C.border}`,borderRadius:8,cursor:"pointer",textAlign:"center"}}><div style={{fontSize:18,marginBottom:3}}>{a.icon}</div><div style={{fontSize:10,fontWeight:700,color:active?a.color:C.muted}}>{a.key}</div></button>);})}</div>
      </div>
      <div style={{display:"grid",gridTemplateColumns:"1fr",gap:10}}>
        <div><div style={{fontSize:11,color:C.dim,fontWeight:600,marginBottom:8}}>PLATFORM-SPECIFIC VOICE</div>
          <div style={{display:"flex",flexDirection:"column",gap:8}}>
            {[{key:"fbTone",label:"📘 Facebook Tone",ph:"e.g. Informative and data-driven with storytelling"},{key:"tiktokTone",label:"🎵 TikTok Tone",ph:"e.g. Energetic, trend-driven, casual hooks"},{key:"ytTone",label:"▶️ YouTube Tone",ph:"e.g. Educational, long-form, expert-level"}].map(f=><FieldInput key={f.key} label={f.label} value={form[f.key]} onChange={v=>s(f.key,v)} placeholder={f.ph}/>)}
          </div>
        </div>
        <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10}}>
          <FieldInput label="✅ Do's" value={form.dos} onChange={v=>s("dos",v)} placeholder="What should AI always do?" multiline rows={3}/>
          <FieldInput label="❌ Don'ts" value={form.donts} onChange={v=>s("donts",v)} placeholder="What should AI never do?" multiline rows={3}/>
        </div>
      </div>
    </div>}

    {/* ── Content Strategy ── */}
    {tab==="content"&&<div style={{display:"flex",flexDirection:"column",gap:14}}>
      <div><div style={{fontSize:11,color:C.dim,fontWeight:600,marginBottom:10}}>CONTENT PILLARS (3 Main Topics)</div>
        <div style={{display:"flex",flexDirection:"column",gap:8}}>
          {[0,1,2].map(i=><div key={i} style={{display:"flex",alignItems:"center",gap:8}}><div style={{width:24,height:24,borderRadius:6,background:`${[C.fb,C.tt,C.green][i]}20`,color:[C.fb,C.tt,C.green][i],fontSize:11,fontWeight:800,display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0}}>{i+1}</div><input value={form.pillars[i]} onChange={e=>{const p=[...form.pillars];p[i]=e.target.value;s("pillars",p);}} placeholder={["e.g. Market Insights & Trends","e.g. Client Success Stories","e.g. Behind the Scenes"][i]} style={{flex:1,background:"#0d1117",border:`1px solid ${form.pillars[i]?C.fb+"60":C.border}`,borderRadius:7,padding:"8px 11px",color:C.text,fontSize:13,outline:"none",fontFamily:"inherit"}}/></div>)}
        </div>
      </div>
      <FieldInput label="Customer Pain Points" value={form.painPoints} onChange={v=>s("painPoints",v)} placeholder="What problems does your target audience face? (AI uses this for hook writing)" multiline rows={3}/>
      <FieldInput label="Content Topic Ideas" value={form.topicIdeas} onChange={v=>s("topicIdeas",v)} placeholder="e.g. Property price comparisons, buyer mistake series, neighborhood guides, investment ROI..." multiline rows={3}/>
    </div>}

    {/* ── Visual Identity ── */}
    {tab==="visual"&&<div style={{display:"flex",flexDirection:"column",gap:16}}>
      <div><label style={{fontSize:10,color:"#9ca3af",fontWeight:600,display:"block",marginBottom:9,letterSpacing:0.5}}>BRAND COLOR PALETTE</label>
        <div style={{display:"flex",gap:9,alignItems:"center",flexWrap:"wrap"}}>
          {form.colors.map((col,i)=>(<div key={i} style={{position:"relative"}}>
            <button onClick={()=>setEditColor(editColor===i?null:i)} style={{width:46,height:46,borderRadius:9,background:col,border:`3px solid ${editColor===i?"#fff":C.border}`,cursor:"pointer",transform:editColor===i?"scale(1.12)":"scale(1)",transition:"transform .15s"}}/>
            <div style={{fontSize:9,color:C.dim,textAlign:"center",marginTop:2,fontFamily:"monospace"}}>{col}</div>
            {editColor===i&&(<div style={{position:"absolute",top:56,left:0,zIndex:50,background:"#1a2235",border:`1px solid ${C.border}`,borderRadius:9,padding:9,width:195,boxShadow:"0 8px 24px #00000080"}}>
              <div style={{display:"flex",flexWrap:"wrap",gap:4,marginBottom:7}}>{PRESET_COLORS.map(pc=><button key={pc} onClick={()=>{const nc=[...form.colors];nc[i]=pc;s("colors",nc);}} style={{width:19,height:19,borderRadius:4,background:pc,border:`2px solid ${pc===col?"#fff":"transparent"}`,cursor:"pointer"}}/>)}</div>
              <input type="color" value={col} onChange={e=>{const nc=[...form.colors];nc[i]=e.target.value;s("colors",nc);}} style={{width:"100%",height:27,borderRadius:5,border:`1px solid ${C.border}`,background:"transparent",cursor:"pointer"}}/>
              <button onClick={()=>setEditColor(null)} style={{marginTop:5,width:"100%",padding:"4px",background:"#374151",border:"none",borderRadius:5,color:C.text,fontSize:11,cursor:"pointer"}}>Done</button>
            </div>)}
          </div>))}
          <div style={{marginLeft:7,flex:1,minWidth:110,height:46,borderRadius:9,background:`linear-gradient(135deg,${form.colors[0]||"#6366f1"},${form.colors[1]||"#ec4899"})`,border:`1px solid ${C.border}`,display:"flex",alignItems:"center",justifyContent:"center"}}>
            <span style={{fontSize:10,color:"rgba(255,255,255,0.8)",fontWeight:700}}>PREVIEW</span>
          </div>
        </div>
      </div>
      <div><label style={{fontSize:10,color:"#9ca3af",fontWeight:600,display:"block",marginBottom:8,letterSpacing:0.5}}>TYPOGRAPHY</label>
        <div style={{display:"flex",gap:7,flexWrap:"wrap"}}>
          {FONT_OPTIONS.map(f=>{const active=form.font===f;const fmap={"Modern Sans":"Inter","Display Serif":"Georgia","Rounded":"Arial Rounded MT Bold","Monospace":"Courier New","Handwritten":"cursive"};return(<button key={f} onClick={()=>s("font",f)} style={{padding:"9px 13px",background:active?C.fb+"18":C.card,border:`2px solid ${active?C.fb:C.border}`,borderRadius:8,cursor:"pointer"}}><div style={{fontFamily:fmap[f],fontSize:15,color:active?C.fb:C.text,marginBottom:2}}>Aa</div><div style={{fontSize:10,color:active?C.fb:C.muted,fontWeight:600}}>{f}</div></button>);})}
        </div>
      </div>
      <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10}}>
        <FieldInput label="Logo Description" value={form.logoDesc} onChange={v=>s("logoDesc",v)} placeholder="e.g. Geometric house icon, navy blue, modern sans-serif" multiline rows={3}/>
        <FieldInput label="Moodboard Keywords" value={form.moodboard} onChange={v=>s("moodboard",v)} placeholder="e.g. trustworthy, modern, clean, premium, urban" multiline rows={3}/>
      </div>
      <div style={{background:`linear-gradient(135deg,${form.colors[0]||"#6366f1"}22,${form.colors[1]||"#ec4899"}11)`,border:`1px solid ${form.colors[0]||C.fb}40`,borderRadius:12,padding:"16px 20px",display:"flex",alignItems:"center",gap:14}}>
        <div style={{width:48,height:48,borderRadius:12,background:`linear-gradient(135deg,${form.colors[0]||"#6366f1"},${form.colors[1]||"#ec4899"})`,display:"flex",alignItems:"center",justifyContent:"center",fontSize:20,flexShrink:0}}>{form.name?form.name[0].toUpperCase():"B"}</div>
        <div><div style={{fontFamily:{"Modern Sans":"Inter","Display Serif":"Georgia","Rounded":"Arial Rounded MT Bold","Monospace":"Courier New","Handwritten":"cursive"}[form.font]||"Inter",fontSize:16,fontWeight:700,color:form.colors[0]||C.fb}}>{form.name||"Brand Name"}</div><div style={{fontSize:11,color:C.muted,marginTop:1}}>{form.industry||"Industry"}</div><div style={{display:"flex",gap:4,marginTop:6}}>{form.colors.map((c,i)=><div key={i} style={{width:12,height:12,borderRadius:3,background:c}}/>)}</div></div>
      </div>
    </div>}

    {/* ── Competitors ── */}
    {tab==="competitors"&&<div style={{display:"flex",flexDirection:"column",gap:11}}>
      <div style={{fontSize:12,color:C.muted,padding:"10px 13px",background:C.card,border:`1px solid ${C.border}`,borderRadius:8}}>AI ကို Brand DNA ကိုသုံးပြီး Content ထုတ်တဲ့အခါ competitor data ကိုရည်ညွှန်းပြီး differentiation strategy ချပေးမည်</div>
      {form.competitors.map((comp,i)=>(<div key={i} style={{background:C.card,border:`1px solid ${C.border}`,borderRadius:9,padding:"11px 13px",display:"flex",gap:10,alignItems:"flex-start"}}><div style={{width:30,height:30,borderRadius:7,background:"#1f2937",display:"flex",alignItems:"center",justifyContent:"center",fontSize:14,flexShrink:0}}>🏢</div><div style={{flex:1}}><div style={{fontSize:13,fontWeight:700,color:C.text}}>{comp.name}</div><div style={{fontSize:11,color:C.muted,marginTop:2}}>{comp.note||"No notes"}</div></div><button onClick={()=>s("competitors",form.competitors.filter((_,j)=>j!==i))} style={{background:"none",border:"none",color:C.dim,cursor:"pointer",fontSize:14,padding:"2px 4px"}}>✕</button></div>))}
      {form.competitors.length===0&&!addingComp&&<div style={{background:C.card,border:`1px dashed ${C.border}`,borderRadius:9,padding:"22px",textAlign:"center",color:C.dim,fontSize:13}}>Competitor မရှိသေး</div>}
      {addingComp?(<div style={{background:C.card,border:`1px solid ${C.fb}40`,borderRadius:9,padding:"12px 13px",display:"flex",flexDirection:"column",gap:8}}>
        <input value={newComp.name} onChange={e=>setNewComp(p=>({...p,name:e.target.value}))} placeholder="Competitor name" style={{background:C.sub,border:`1px solid ${C.border}`,borderRadius:7,padding:"7px 10px",color:C.text,fontSize:13,outline:"none",fontFamily:"inherit"}}/>
        <textarea value={newComp.note} onChange={e=>setNewComp(p=>({...p,note:e.target.value}))} placeholder="Strengths / Weaknesses / Notes" rows={2} style={{background:C.sub,border:`1px solid ${C.border}`,borderRadius:7,padding:"7px 10px",color:C.text,fontSize:13,outline:"none",resize:"none",fontFamily:"inherit"}}/>
        <div style={{display:"flex",gap:7}}><button onClick={()=>{if(newComp.name.trim()){s("competitors",[...form.competitors,newComp]);setNewComp({name:"",note:""});setAddingComp(false);}}} style={{padding:"6px 15px",background:C.fb,border:"none",borderRadius:7,color:"#fff",fontWeight:700,fontSize:12,cursor:"pointer"}}>Add</button><button onClick={()=>{setAddingComp(false);setNewComp({name:"",note:""}); }} style={{padding:"6px 15px",background:"transparent",border:`1px solid ${C.border}`,borderRadius:7,color:C.muted,fontSize:12,cursor:"pointer"}}>Cancel</button></div>
      </div>):(
        <button onClick={()=>setAddingComp(true)} style={{padding:"9px",background:"transparent",border:`1px dashed #374151`,borderRadius:8,color:C.muted,fontSize:12,fontWeight:600,cursor:"pointer",display:"flex",alignItems:"center",justifyContent:"center",gap:5}}>+ Add Competitor</button>
      )}
    </div>}
  </>);
}

function BrandPage({client}){
  const init=client!=="All Clients"?(SAMPLE_BRANDS[client]||{...EMPTY_BRAND}):{...EMPTY_BRAND};
  const [form,setForm]=useState(init);
  const [mode,setMode]=useState("manual"); // "manual" | "ai"
  const [saved,setSaved]=useState(false);

  useEffect(()=>{setForm(client!=="All Clients"?(SAMPLE_BRANDS[client]||{...EMPTY_BRAND}):{...EMPTY_BRAND});setSaved(false);},[client]);

  const completionKeys=["name","industry","audience","usp","mission","promise","tone","archetype"];
  const completion=Math.round((completionKeys.filter(k=>form[k]).length/completionKeys.length)*100);
  const save=()=>{setSaved(true);setTimeout(()=>setSaved(false),2500);};

  const applyAI=(data)=>{setForm(f=>({...f,...data}));setMode("manual");};

  if(client==="All Clients")return(
    <div style={{display:"flex",flexDirection:"column",gap:14}}>
      <div><h1 style={{fontSize:20,fontWeight:700,color:C.head,margin:"0 0 4px"}}>🧬 Brand DNA</h1><p style={{color:C.muted,fontSize:13,margin:0}}>Client တစ်ဦးကို ရွေးချယ်ပြီး Brand DNA Configure လုပ်ပါ</p></div>
      <div style={{background:C.card,border:`1px solid ${C.border}`,borderRadius:12,padding:"28px 22px",textAlign:"center"}}><div style={{fontSize:36,marginBottom:9}}>🧬</div><div style={{fontSize:14,color:C.text,fontWeight:600,marginBottom:5}}>Client မရွေးရသေးပါ</div><div style={{fontSize:12,color:C.muted}}>Top bar ရှိ Client Picker ကိုသုံးပြီး Client တစ်ဦးရွေးပါ</div></div>
    </div>
  );

  return(
    <div style={{display:"flex",flexDirection:"column",gap:16}}>
      {/* Header */}
      <div style={{display:"flex",alignItems:"flex-start",justifyContent:"space-between",flexWrap:"wrap",gap:10}}>
        <div><h1 style={{fontSize:20,fontWeight:700,color:C.head,margin:"0 0 3px"}}>🧬 Brand DNA</h1><p style={{color:C.muted,fontSize:13,margin:0}}>{form.name||client}</p></div>
        <div style={{display:"flex",alignItems:"center",gap:9}}>
          <div style={{display:"flex",alignItems:"center",gap:7,background:C.card,border:`1px solid ${C.border}`,borderRadius:8,padding:"5px 11px"}}>
            <div style={{position:"relative",width:24,height:24}}>
              <svg width="24" height="24" viewBox="0 0 24 24" style={{transform:"rotate(-90deg)"}}>
                <circle cx="12" cy="12" r="9" fill="none" stroke={C.border} strokeWidth="3"/>
                <circle cx="12" cy="12" r="9" fill="none" stroke={completion===100?C.green:C.fb} strokeWidth="3" strokeDasharray={`${2*Math.PI*9}`} strokeDashoffset={`${2*Math.PI*9*(1-completion/100)}`} strokeLinecap="round"/>
              </svg>
              <div style={{position:"absolute",inset:0,display:"flex",alignItems:"center",justifyContent:"center",fontSize:7,fontWeight:800,color:completion===100?C.green:C.fb}}>{completion}%</div>
            </div>
            <div><div style={{fontSize:9,color:C.dim,fontWeight:600}}>PROFILE</div><div style={{fontSize:10,color:completion===100?C.green:C.text,fontWeight:700}}>{completion===100?"Complete":"Incomplete"}</div></div>
          </div>
          {mode==="manual"&&<button onClick={save} style={{padding:"7px 16px",background:saved?"#10b981":"#6366f1",border:"none",borderRadius:8,color:"#fff",fontWeight:700,fontSize:12,cursor:"pointer",transition:"background .2s"}}>{saved?"✓ Saved":"💾 Save"}</button>}
        </div>
      </div>

      {/* Mode Switcher */}
      <div style={{display:"flex",gap:0,background:C.card,border:`1px solid ${C.border}`,borderRadius:11,padding:4}}>
        <button onClick={()=>setMode("manual")} style={{flex:1,padding:"9px 14px",borderRadius:8,border:"none",cursor:"pointer",fontSize:13,fontWeight:700,background:mode==="manual"?"#1f2937":"transparent",color:mode==="manual"?C.head:C.muted,display:"flex",alignItems:"center",justifyContent:"center",gap:7,transition:"all .15s"}}>
          <span>✍️</span> Manual Mode
          {mode==="manual"&&<span style={{fontSize:10,background:"#6366f130",color:"#818cf8",padding:"1px 7px",borderRadius:99}}>Active</span>}
        </button>
        <button onClick={()=>setMode("ai")} style={{flex:1,padding:"9px 14px",borderRadius:8,border:"none",cursor:"pointer",fontSize:13,fontWeight:700,background:mode==="ai"?"linear-gradient(135deg,#6366f130,#8b5cf630)":"transparent",color:mode==="ai"?"#a78bfa":C.muted,display:"flex",alignItems:"center",justifyContent:"center",gap:7,transition:"all .15s"}}>
          <span>🤖</span> AI Generate
          {mode==="ai"&&<span style={{fontSize:10,background:"#8b5cf630",color:"#a78bfa",padding:"1px 7px",borderRadius:99}}>Active</span>}
        </button>
      </div>

      {mode==="manual"&&<ManualMode form={form} setF={setForm} client={client}/>}
      {mode==="ai"&&<AIGenerateMode onApply={applyAI} client={client}/>}

      {/* Footer */}
      {mode==="manual"&&<div style={{display:"flex",alignItems:"center",justifyContent:"space-between",padding:"10px 14px",background:C.card,border:`1px solid ${C.border}`,borderRadius:9,marginTop:2}}>
        <div style={{fontSize:11,color:C.dim}}>🔗 Phase 3 — AI က Brand DNA ကိုဖတ်ပြီး <span style={{color:C.text,fontWeight:600}}>{client}</span> အတွက် content ထုတ်မည်</div>
        <button onClick={save} style={{padding:"6px 16px",background:saved?"#10b981":"#6366f1",border:"none",borderRadius:7,color:"#fff",fontWeight:700,fontSize:12,cursor:"pointer",transition:"background .2s"}}>{saved?"✓ Saved!":"💾 Save"}</button>
      </div>}
    </div>
  );
}

function ContentPage(){const steps=[{n:"01",label:"Strategy",desc:"AI analyzes brand + trends",icon:"🧠",st:"Ready"},{n:"02",label:"Hook Generation",desc:"Scroll-stopping hooks per platform",icon:"🪝",st:"Ready"},{n:"03",label:"Script Writing",desc:"Full scripts from strategy",icon:"📝",st:"Ready"},{n:"04",label:"Visual Direction",desc:"Shot list, B-roll, thumbnails",icon:"🎨",st:"Ready"},{n:"05",label:"Review & Approve",desc:"CEO reviews before publishing",icon:"✅",st:"Pending CEO"},{n:"06",label:"One-Click Publish",desc:"Auto-post to all platforms",icon:"🚀",st:"Phase 4"}];const sc={Ready:C.green,"Pending CEO":C.amber,"Phase 4":C.dim};const sb={Ready:"#10b98115","Pending CEO":"#f59e0b15","Phase 4":C.border};return(<div><h1 style={{fontSize:20,fontWeight:700,color:C.head,margin:"0 0 5px"}}>✍️ Content Creation</h1><p style={{color:C.muted,fontSize:13,margin:"0 0 13px"}}>AI-powered pipeline — strategy to publish.</p><div style={{display:"flex",flexDirection:"column",gap:7}}>{steps.map((p,i)=>(<div key={i} style={{background:C.card,border:`1px solid ${C.border}`,borderRadius:9,padding:"11px 13px",display:"flex",gap:11,alignItems:"center"}}><span style={{fontSize:10,color:C.dim,fontWeight:700,minWidth:20}}>{p.n}</span><span style={{fontSize:17,minWidth:22}}>{p.icon}</span><div style={{flex:1}}><div style={{fontSize:13,fontWeight:700,color:C.text}}>{p.label}</div><div style={{fontSize:11,color:C.muted,marginTop:2}}>{p.desc}</div></div><span style={{fontSize:10,padding:"3px 9px",borderRadius:99,background:sb[p.st],color:sc[p.st],fontWeight:600,whiteSpace:"nowrap"}}>{p.st}</span></div>))}</div></div>);}
function ArchivePage(){const p=[{name:"Project Alpha — Real Estate",date:"Feb 2026",platform:"Facebook",status:"Completed",posts:12},{name:"Fashion Brand Launch",date:"Mar 2026",platform:"TikTok",status:"Active",posts:6},{name:"Restaurant Chain Weekly",date:"Jan 2026",platform:"Facebook",status:"Completed",posts:28}];return(<div><h1 style={{fontSize:20,fontWeight:700,color:C.head,margin:"0 0 5px"}}>🗂️ Project Archive</h1><p style={{color:C.muted,fontSize:13,margin:"0 0 13px"}}>All client campaigns.</p><div style={{display:"flex",flexDirection:"column",gap:7}}>{p.map((x,i)=>(<div key={i} style={{background:C.card,border:`1px solid ${C.border}`,borderRadius:9,padding:"11px 13px",display:"flex",justifyContent:"space-between",alignItems:"center"}}><div><div style={{fontSize:13,fontWeight:600,color:C.text}}>{x.name}</div><div style={{fontSize:11,color:C.muted,marginTop:3}}>{x.date} · {x.platform} · {x.posts} posts</div></div><span style={{fontSize:10,padding:"3px 9px",borderRadius:99,background:x.status==="Active"?"#6366f115":"#1f2937",color:x.status==="Active"?"#818cf8":C.dim,fontWeight:600}}>{x.status}</span></div>))}<button style={{marginTop:4,padding:"8px 14px",background:"transparent",border:`1px dashed #374151`,borderRadius:7,color:C.muted,fontSize:12,fontWeight:600,cursor:"pointer",width:"fit-content"}}>+ New Project</button></div></div>);}
function AssetsPage(){const cats=["All","Logos","Images","Videos","Templates","Copy"];const [cat,setCat]=useState("All");return(<div><h1 style={{fontSize:20,fontWeight:700,color:C.head,margin:"0 0 5px"}}>🖼️ Assets Library</h1><p style={{color:C.muted,fontSize:13,margin:"0 0 13px"}}>Brand assets & generated content.</p><div style={{display:"flex",gap:5,marginBottom:13,flexWrap:"wrap"}}>{cats.map(c=><button key={c} onClick={()=>setCat(c)} style={{padding:"4px 11px",borderRadius:99,border:"1px solid",borderColor:cat===c?"#6366f1":C.border,background:cat===c?"#6366f115":"transparent",color:cat===c?"#818cf8":C.muted,fontSize:12,fontWeight:600,cursor:"pointer"}}>{c}</button>)}</div><div style={{display:"grid",gridTemplateColumns:"repeat(auto-fill,minmax(100px,1fr))",gap:7}}>{Array.from({length:6}).map((_,i)=>(<div key={i} style={{background:C.card,border:`1px solid ${C.border}`,borderRadius:8,aspectRatio:"1",display:"flex",flexDirection:"column",alignItems:"center",justifyContent:"center",gap:5,cursor:"pointer"}}><span style={{fontSize:22}}>📁</span><span style={{fontSize:10,color:C.dim}}>Asset {i+1}</span></div>))}<div style={{background:C.card,border:`1px dashed #374151`,borderRadius:8,aspectRatio:"1",display:"flex",flexDirection:"column",alignItems:"center",justifyContent:"center",cursor:"pointer"}}><span style={{fontSize:22,color:"#374151"}}>+</span><span style={{fontSize:10,color:C.dim,marginTop:2}}>Upload</span></div></div></div>);}
function CreatorPage(){const pl=[{name:"YouTube",icon:"▶️",color:C.yt},{name:"TikTok",icon:"🎵",color:C.tt},{name:"Facebook",icon:"📘",color:C.fb}];return(<div><h1 style={{fontSize:20,fontWeight:700,color:C.head,margin:"0 0 5px"}}>🎬 Creator Mode</h1><p style={{color:C.muted,fontSize:13,margin:"0 0 13px"}}>Faceless content engine for passive income.</p><div style={{background:C.card,border:"1px solid #6366f130",borderRadius:10,padding:13,marginBottom:13}}><div style={{fontSize:13,fontWeight:600,color:"#818cf8",marginBottom:3}}>🤖 AI Topic Generator</div><div style={{color:C.dim,fontSize:13}}>Auto-generate faceless content scripts per platform. (Phase 4)</div></div><div style={{display:"flex",flexDirection:"column",gap:7}}>{pl.map(p=>(<div key={p.name} style={{background:C.card,border:`1px solid ${C.border}`,borderRadius:9,padding:"11px 13px",display:"flex",justifyContent:"space-between",alignItems:"center"}}><div style={{display:"flex",gap:9,alignItems:"center"}}><span style={{fontSize:18}}>{p.icon}</span><div><div style={{fontSize:13,fontWeight:600,color:C.text}}>{p.name}</div><div style={{fontSize:11,color:C.muted}}>Monetization · Sponsorships · Faceless</div></div></div><button style={{padding:"5px 11px",borderRadius:7,border:`1px solid ${p.color}50`,background:p.color+"15",color:p.color,fontSize:12,fontWeight:600,cursor:"pointer"}}>Connect</button></div>))}</div></div>);}
function StatusPage(){const it=[{name:"AI Engine",status:"Online",ok:true},{name:"Facebook API",status:"Connected",ok:true},{name:"TikTok API",status:"Connected",ok:true},{name:"YouTube API",status:"Standby",ok:false},{name:"Auto-Publish",status:"Active",ok:true},{name:"News Feed",status:"Live",ok:true}];return(<div><h1 style={{fontSize:20,fontWeight:700,color:C.head,margin:"0 0 5px"}}>🛰️ System Status</h1><p style={{color:C.muted,fontSize:13,margin:"0 0 13px"}}>Real-time health of all services.</p><div style={{display:"flex",flexDirection:"column",gap:6}}>{it.map((s,i)=>(<div key={i} style={{background:C.card,border:`1px solid ${C.border}`,borderRadius:8,padding:"10px 13px",display:"flex",justifyContent:"space-between",alignItems:"center"}}><span style={{fontSize:13,color:C.text,fontWeight:500}}>{s.name}</span><div style={{display:"flex",alignItems:"center",gap:5}}><span style={{width:6,height:6,borderRadius:"50%",background:s.ok?C.green:C.amber,boxShadow:`0 0 5px ${s.ok?C.green:C.amber}90`}}/><span style={{fontSize:12,color:s.ok?C.green:C.amber,fontWeight:600}}>{s.status}</span></div></div>))}</div><div style={{marginTop:11,background:"#10b98108",border:"1px solid #10b98130",borderRadius:8,padding:"9px 12px",fontSize:12,color:C.muted}}>Last checked: <span style={{color:C.green}}>Just now</span> · All core systems operational.</div></div>);}

const NAV_LABEL={news:"Industry News & Trends",dashboard:"Interactive Dashboard",brand:"Brand DNA",content:"Content Creation",archive:"Project Archive",assets:"Assets Library",creator:"Creator Mode",status:"System Status"};

export default function App(){
  const [active,setActive]=useState("dashboard");const [menuOpen,setMenuOpen]=useState(true);const [client,setClient]=useState("All Clients");const [clientOpen,setClientOpen]=useState(false);const [voicePlatform,setVoicePlatform]=useState(null);const [voiceTf,setVoiceTf]=useState(null);
  const handleAgentCommand=useCallback((cmd)=>{if(cmd.type==="navigate"){setActive(cmd.page);}else if(cmd.type==="client"){setClient(cmd.value);}else if(cmd.type==="platform"){setActive("dashboard");setVoicePlatform(cmd.value);setTimeout(()=>setVoicePlatform(null),500);}else if(cmd.type==="timeframe"){setVoiceTf(cmd.value);setTimeout(()=>setVoiceTf(null),500);}},[]);
  const SI=({id,icon,label,sub})=>{const on=active===id;return(<button onClick={()=>setActive(id)} style={{display:"flex",alignItems:"center",gap:7,padding:sub?"7px 8px 7px 26px":"8px 10px",borderRadius:7,border:"none",background:on?"#6366f118":"transparent",color:on?"#818cf8":C.muted,fontWeight:on?600:400,fontSize:12,width:"100%",cursor:"pointer",textAlign:"left"}}><span style={{fontSize:13}}>{icon}</span><span style={{flex:1,whiteSpace:"nowrap",overflow:"hidden",textOverflow:"ellipsis"}}>{label}</span>{on&&<span style={{width:3,height:12,background:"#6366f1",borderRadius:2,flexShrink:0}}/>}</button>);};
  const PageComponent=active==="dashboard"?<DashboardPage client={client} voicePlatform={voicePlatform} voiceTf={voiceTf}/>:{news:<NewsPage/>,brand:<BrandPage client={client}/>,content:<ContentPage/>,archive:<ArchivePage/>,assets:<AssetsPage/>,creator:<CreatorPage/>,status:<StatusPage/>}[active]||<DashboardPage client={client}/>;
  return(
    <div style={{display:"flex",height:"100vh",background:C.bg,fontFamily:"'Inter',-apple-system,sans-serif",color:C.text,overflow:"hidden"}}>
      <div style={{width:214,minWidth:214,background:C.sub,borderRight:`1px solid ${C.border}`,display:"flex",flexDirection:"column",height:"100vh",overflowY:"auto",padding:"0 6px 12px"}}>
        <div style={{padding:"13px 10px 11px",borderBottom:`1px solid ${C.border}`,marginBottom:4}}><div style={{display:"flex",alignItems:"center",gap:8}}><div style={{width:28,height:28,borderRadius:7,background:"linear-gradient(135deg,#6366f1,#ec4899)",display:"flex",alignItems:"center",justifyContent:"center",fontSize:13}}>⚡</div><div><div style={{fontSize:11,fontWeight:800,color:C.head,lineHeight:1.2}}>Sayar Gyi's</div><div style={{fontSize:9,color:C.muted}}>AI Command Center</div></div></div></div>
        <div style={{flex:1,display:"flex",flexDirection:"column",gap:1}}>
          <SI id="news" icon="📡" label="Industry News & Trends"/>
          <div><button onClick={()=>setMenuOpen(o=>!o)} style={{display:"flex",alignItems:"center",gap:7,padding:"6px 10px",borderRadius:7,border:"none",background:"transparent",color:C.dim,fontSize:9,fontWeight:700,width:"100%",cursor:"pointer",letterSpacing:1,textTransform:"uppercase"}}><span>MENU</span><span style={{marginLeft:"auto",transform:menuOpen?"rotate(90deg)":"rotate(0)",transition:".2s",fontSize:9}}>▶</span></button>{menuOpen&&<div style={{display:"flex",flexDirection:"column",gap:1}}><SI id="dashboard" icon="📊" label="Interactive Dashboard" sub/><SI id="brand" icon="🧬" label="Brand DNA" sub/><SI id="content" icon="✍️" label="Content Creation" sub/><SI id="archive" icon="🗂️" label="Project Archive" sub/><SI id="assets" icon="🖼️" label="Assets Library" sub/></div>}</div>
          <div style={{borderTop:`1px solid ${C.border}`,margin:"5px 0"}}/><SI id="creator" icon="🎬" label="Creator Mode"/><SI id="status" icon="🛰️" label="System Status"/>
        </div>
        <div style={{borderTop:`1px solid ${C.border}`,padding:"9px 10px 0",marginTop:4}}><div style={{display:"flex",alignItems:"center",gap:7}}><div style={{width:24,height:24,borderRadius:"50%",background:"linear-gradient(135deg,#6366f1,#ec4899)",display:"flex",alignItems:"center",justifyContent:"center",fontSize:11}}>👤</div><div><div style={{fontSize:11,color:C.head,fontWeight:600}}>Sayar Gyi</div><div style={{fontSize:9,color:C.green}}>● CEO / Admin</div></div></div></div>
      </div>
      <div style={{flex:1,display:"flex",flexDirection:"column",overflow:"hidden"}}>
        <div style={{background:C.sub,borderBottom:`1px solid ${C.border}`,padding:"0 16px",height:43,display:"flex",alignItems:"center",justifyContent:"space-between",flexShrink:0}}>
          <div style={{display:"flex",alignItems:"center",gap:6}}><span style={{fontSize:11,color:C.dim}}>AI Command Center</span><span style={{color:"#374151"}}>/</span><span style={{fontSize:11,color:"#9ca3af",fontWeight:600}}>{NAV_LABEL[active]}</span></div>
          <div style={{display:"flex",alignItems:"center",gap:8}}>
            <div style={{position:"relative"}}><button onClick={()=>setClientOpen(o=>!o)} style={{display:"flex",alignItems:"center",gap:5,padding:"3px 9px",background:clientOpen?"#1f2937":"transparent",border:`1px solid ${clientOpen?C.fb+"60":C.border}`,borderRadius:6,cursor:"pointer",color:client==="All Clients"?C.muted:C.fb,fontSize:11,fontWeight:600}}><span>👤</span><span style={{maxWidth:90,overflow:"hidden",textOverflow:"ellipsis",whiteSpace:"nowrap"}}>{client}</span><span style={{fontSize:9,color:C.dim,transform:clientOpen?"rotate(180deg)":"rotate(0)",transition:".15s"}}>▾</span></button>{clientOpen&&<div style={{position:"absolute",top:"calc(100% + 4px)",right:0,background:"#1a2235",border:`1px solid ${C.border}`,borderRadius:8,padding:4,zIndex:200,minWidth:148,boxShadow:"0 8px 24px #00000060"}}>{CLIENTS.map(cl=><button key={cl} onClick={()=>{setClient(cl);setClientOpen(false);}} style={{display:"block",width:"100%",padding:"6px 10px",border:"none",background:client===cl?"#6366f120":"transparent",color:client===cl?"#818cf8":C.muted,fontSize:11,fontWeight:client===cl?700:400,cursor:"pointer",textAlign:"left",borderRadius:5}}>{cl==="All Clients"?`🌐 ${cl}`:`👤 ${cl}`}</button>)}</div>}</div>
            <div style={{display:"flex",gap:4,alignItems:"center"}}><span style={{width:6,height:6,borderRadius:"50%",background:C.green,boxShadow:"0 0 5px #10b98180"}}/><span style={{fontSize:11,color:C.green}}>Online</span></div>
          </div>
        </div>
        <div style={{flex:1,overflowY:"auto",padding:16}} onClick={()=>clientOpen&&setClientOpen(false)}>{PageComponent}</div>
      </div>
      <FloatingMusic/><FloatingAgent onCommand={handleAgentCommand}/>
    </div>
  );
}
