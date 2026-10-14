# caveman-th

สกิลประหยัด token สำหรับผู้ใช้ภาษาไทย ดัดแปลงแนวคิดจาก [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) (Apache-2.0)

## หลักการ
- เอเจนต์คิด เรียก tool และส่งงานต่อให้เอเจนต์อื่นเป็นภาษาอังกฤษแบบห้วน
- ตอบผู้ใช้เป็นภาษาไทยแบบห้วนเฉพาะข้อความสุดท้าย: ไม่ใส่ ครับ/ค่ะ ไม่ใช้คำฟุ่มเฟือย ใช้ศัพท์เทคนิคภาษาอังกฤษ ตอบเป็น bullet ไม่เกิน 3 บรรทัด

## ติดตั้ง
คัดลอก `SKILL.md` ไปไว้ในโฟลเดอร์ skills ของเอเจนต์ เช่น `~/.claude/skills/caveman-th/SKILL.md` หรือ `.cursor/skills/caveman-th/SKILL.md`

## ผลวัด token (tiktoken)
ใช้ตัวอย่างคำตอบของบอท Dev 5 ข้อความ รันซ้ำได้ด้วย `pip install tiktoken && python measure.py`

| encoding | ไทยปกติ | ไทยห้วน | ประหยัด | EN caveman | ประหยัดเมื่อเทียบกับไทยปกติ |
|---|---|---|---|---|---|
| o200k_base | 395 | 154 | 61.0% | 120 | 69.6% |
| cl100k_base | 934 | 269 | 71.2% | 119 | 87.3% |

ผลแยกรายข้อความดูได้ที่ `results.md`

## เครดิตและสัญญาอนุญาต
ดัดแปลงจาก caveman โดย Julius Brussee, Apache License 2.0 (ดูไฟล์ `LICENSE` และ `NOTICE-upstream`) ไฟล์ SKILL.md เขียนขึ้นใหม่ ไม่ได้คัดลอกโค้ด proxy มา
