#!/usr/bin/env python3
import json, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "yt-edit"))
from deadair import load
STOP=set("the a an of for to in on and or is are was were be been with this that it as at by from you your i my we our they them he she but so if then than there here what which who how when where why not no yes do does did just really very like about into over out up down can could will would should have has had get got make made go going went one two".split())
def keywords(text): return {w for w in re.findall(r"[a-z']{4,}",text.lower()) if w not in STOP}
def mmss(t):
 t=int(t); h,m,s=t//3600,(t%3600)//60,t%60; return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"
def main():
 a=sys.argv[1:]; as_json="--json" in a; a=[x for x in a if x!="--json"]; target=int(a[a.index("--target")+1]) if "--target" in a else 7; files=[x for x in a if not x.startswith("--") and not x.isdigit()]
 if not files or not os.path.exists(files[0]): sys.exit(1)
 cues=load(files[0]); dur=cues[-1][1]; cand=[]
 for i in range(1,len(cues)):
  gap=cues[i][0]-cues[i-1][1]; before=" ".join(c[2] for c in cues[max(0,i-12):i]); after=" ".join(c[2] for c in cues[i:i+12]); kb,ka=keywords(before),keywords(after); shift=1-(len(kb&ka)/len(kb|ka)) if kb|ka else 0; cand.append((gap*1.6+shift*3.2,cues[i][0]))
 cand.sort(reverse=True); picked=[0.0]
 for _,t in cand:
  if len(picked)>=target: break
  if all(abs(t-p)>=10 for p in picked) and dur-t>=10: picked.append(t)
 picked.sort(); chapters=[]
 for n,t in enumerate(picked):
  end=picked[n+1] if n+1<len(picked) else dur; text=" ".join(c[2] for c in cues if c[0]>=t and c[1]<=end); kw=sorted(keywords(text),key=lambda w:-text.lower().count(w)); chapters.append({"start":round(t,2),"label":mmss(t),"draft_title":" ".join(w.capitalize() for w in kw[:3]) or "Section","seconds":round(end-t,2)})
 ok=len(chapters)>=3 and chapters[0]["start"]==0 and all(c["seconds"]>=10 for c in chapters)
 if as_json: print(json.dumps({"valid":ok,"chapters":chapters},indent=1)); return
 for c in chapters: print(f"{c['label']} {c['draft_title']}")
 print(f"{len(chapters)} chapters"+("" if ok else " -- INVALID"))
if __name__=="__main__": main()