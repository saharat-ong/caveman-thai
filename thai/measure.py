import tiktoken
E=[tiktoken.get_encoding(n) for n in ("o200k_base","cl100k_base")]
S=[
("ผมได้ทำการตรวจสอบ bug ที่คุณแจ้งมาเป็นที่เรียบร้อยแล้วครับ ปัญหาเกิดจากในส่วนของ middleware ที่ใช้ตรวจสอบ token ซึ่งใช้เครื่องหมาย < แทนที่จะเป็น <= ทำให้ token ที่หมดอายุพอดีไม่ถูกปฏิเสธครับ ผมได้ทำการแก้ไขและเปิด PR #142 ไว้ให้แล้ว รบกวนช่วยรีวิวด้วยนะครับ",
 "- bug อยู่ที่ auth middleware: ใช้ `<` แทน `<=` token หมดอายุพอดีเลยผ่าน\n- fix แล้ว เปิด PR #142 รอ review",
 "Bug in auth middleware: `<` not `<=`, expired-at-boundary token passes. Fixed in PR #142. Needs review."),
("ตอนนี้ผมได้ทำการ deploy เวอร์ชัน v2.3.1 ขึ้น staging เป็นที่เรียบร้อยแล้วครับ โดยที่ test ทั้งหมด 214 ตัวผ่านหมด ไม่มีตัวไหน fail เลยครับ ถ้าคุณต้องการ ผมสามารถ deploy ขึ้น production ต่อได้เลยครับ",
 "- deploy v2.3.1 ขึ้น staging แล้ว test ผ่าน 214/214\n- deploy production ต่อไหม",
 "v2.3.1 on staging. Tests 214/214 pass. Deploy to production?"),
("ผมได้ลองรัน build แล้วครับ แต่ build ไม่ผ่านเนื่องจากมี error ว่า `Cannot find module 'zod'` ซึ่งน่าจะเกิดจากการที่ในส่วนของ package.json ยังไม่ได้มีการเพิ่ม dependency ตัวนี้เข้าไปครับ ผมแนะนำให้รัน `pnpm add zod` แล้วลอง build ใหม่อีกครั้งครับ",
 "- build fail: `Cannot find module 'zod'` ยังไม่มีใน package.json\n- แก้: `pnpm add zod` แล้ว build ใหม่",
 "Build fails: `Cannot find module 'zod'`. Missing from package.json. Run `pnpm add zod`, rebuild."),
("สำหรับคำถามเรื่องการเลือกฐานข้อมูลนะครับ ผมคิดว่าในกรณีของโปรเจกต์นี้ PostgreSQL น่าจะเหมาะสมกว่า MongoDB ครับ เนื่องจากข้อมูลของเรามีความสัมพันธ์กันค่อนข้างมาก และต้องการ transaction ที่มีความถูกต้องสูง อย่างไรก็ตาม ถ้าในอนาคตมีข้อมูลที่ไม่มีโครงสร้างตายตัว เราก็สามารถใช้ JSONB ใน PostgreSQL ได้ครับ",
 "- ใช้ PostgreSQL: ข้อมูล relational เยอะ ต้องการ transaction\n- ข้อมูลไม่มี schema ตายตัวใช้ JSONB ได้",
 "PostgreSQL. Data is relational, needs transactions. Unstructured data later: use JSONB."),
("ผมได้ทำการตรวจสอบ log ของ server ในช่วง 1 ชั่วโมงที่ผ่านมาแล้วครับ พบว่ามี error 502 เกิดขึ้นทั้งหมด 37 ครั้ง ซึ่งทั้งหมดเกิดขึ้นในช่วงที่ CPU ของ pod ขึ้นไปถึง 100% ครับ ผมคิดว่าเราควรเพิ่ม resource limit หรือตั้งค่า autoscaling ให้กับ deployment นี้ครับ",
 "- 1 ชม.ล่าสุด 502 รวม 37 ครั้ง ทุกครั้งตอน pod CPU 100%\n- แนะนำเพิ่ม resource limit หรือเปิด HPA",
 "Last 1h: 37x 502, all at pod CPU 100%. Raise resource limits or enable HPA."),
]
tot=[[0,0,0],[0,0,0]]
print("| # | enc | ไทยปกติ | ไทยห้วน | ประหยัด | EN caveman | vs ไทยปกติ |")
print("|---|---|---|---|---|---|---|")
for i,s in enumerate(S,1):
  for j,e in enumerate(E):
    c=[len(e.encode(x)) for x in s]
    for k in range(3): tot[j][k]+=c[k]
    print(f"| {i} | {e.name} | {c[0]} | {c[1]} | {100*(1-c[1]/c[0]):.0f}% | {c[2]} | {100*(1-c[2]/c[0]):.0f}% |")
for j,e in enumerate(E):
  c=tot[j]; print(f"| รวม | {e.name} | {c[0]} | {c[1]} | {100*(1-c[1]/c[0]):.1f}% | {c[2]} | {100*(1-c[2]/c[0]):.1f}% |")
