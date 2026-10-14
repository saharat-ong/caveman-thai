🇬🇧 [Read in English](README.md)

<a id="caveman-th"></a>
## 🇹🇭 caveman-th: เวอร์ชันภาษาไทย (โฟลเดอร์ [`thai/`](./thai/))

repo นี้ fork มาจาก [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) แล้วเพิ่มสกิล `caveman-th` สำหรับคนที่ใช้เอเจนต์เป็นภาษาไทย

**ทำอะไร:** ภาษาไทยใช้ token ต่อความหมายมากกว่าภาษาอังกฤษ 2-4 เท่า สกิลนี้เลยให้เอเจนต์คิด เรียก tool และส่งงานต่อให้เอเจนต์อื่นเป็นภาษาอังกฤษแบบห้วน ส่วนคำตอบสุดท้ายที่คนอ่านจะเป็นภาษาไทยแบบห้วน คือไม่มี ครับ/ค่ะ ไม่มีคำฟุ่มเฟือยอย่าง "ได้ทำการ" "ในส่วนของ" "เป็นที่เรียบร้อย" ใช้ศัพท์เทคนิคเป็นภาษาอังกฤษ (deploy, PR) ตอบเป็น bullet ไม่เกิน 3 บรรทัด และไม่ทวนคำถาม

**ติดตั้งสกิล:** คัดลอก [`thai/SKILL.md`](./thai/SKILL.md) ไปไว้ในโฟลเดอร์ skills ของเอเจนต์

```bash
mkdir -p ~/.claude/skills/caveman-th && cp thai/SKILL.md ~/.claude/skills/caveman-th/SKILL.md
# หรือสำหรับ Cursor ในโปรเจกต์
mkdir -p .cursor/skills/caveman-th && cp thai/SKILL.md .cursor/skills/caveman-th/SKILL.md
```

สกิลนี้เป็นข้อความคำสั่งอย่างเดียว ไม่ต้องติดตั้ง CLI หรือ proxy

**ผลวัด token** (tiktoken, คำตอบของบอท Dev 5 ข้อความ, รันซ้ำได้ด้วย `pip install tiktoken && python thai/measure.py`)

| encoding | ไทยปกติ | ไทยห้วน | ประหยัด | EN caveman | EN caveman เทียบไทยปกติ |
|---|---:|---:|---:|---:|---:|
| o200k_base | 395 | 154 | **61.0%** | 120 | 69.6% |
| cl100k_base | 934 | 269 | **71.2%** | 119 | 87.3% |

ผลรายข้อความอยู่ที่ [`thai/results.md`](./thai/results.md) ตัวเลขนี้วัดเฉพาะคำตอบสุดท้าย งานจริงน่าจะประหยัดได้มากกว่านี้ เพราะส่วนคิดและการเรียก tool ใช้ภาษาอังกฤษอยู่แล้ว

**ข้อควรระวังเรื่อง proxy และ CLI ของ upstream** (ไม่เกี่ยวกับตัวสกิล ซึ่งไม่ส่งข้อมูลออกไปไหน)
- **telemetry ของ CLI เปิดเป็นค่าเริ่มต้น** ส่งสถิติการใช้งาน (คำสั่ง จำนวน token, install ID, OS, IP) ไปที่ Supabase ของ Caveman ไม่ส่ง prompt หรือโค้ด ปิดได้ด้วย `caveman telemetry off` หรือ `DO_NOT_TRACK=1` ถ้ารัน `caveman-proxy serve` ตรง ๆ จะไม่มี telemetry
- **Auto routing** (เมื่อ login และเลือก Auto) ส่งข้อความล่าสุดของคุณแบบดิบไปให้ Caveman Cloud รวมถึง CLAUDE.md ไฟล์ที่ @ ถึง และ output ของ shell ถ้าใช้แผน Free ทาง Caveman อาจเก็บข้อมูลไว้ ปิดด้วย `caveman off routing`
- **โมเดลของ Caveman Cloud** (`via: cloud`) ส่ง request ทั้งก้อน (system prompt, tool result, โค้ด) ผ่าน Caveman Cloud ปิดด้วย `caveman providers cloud off`
- **managed gateway** ส่งทุก request ผ่าน Caveman Cloud พร้อมชื่อ repo และ branch ใน `x-cave-tags` ปิด tag ด้วย `CAVEMAN_WORK_TAGS=0`
- **warm cache** (`waste-fixes`) ส่ง request ซ้ำไปที่ Anthropic เพื่อให้ cache ไม่หมดอายุ ปิดด้วย `CAVEMAN_CACHE_WARM=off` หรือ `caveman off waste-fixes`
- proxy ไม่มีการยืนยันตัวตนเป็นค่าเริ่มต้น ให้ bind ไว้ที่ `127.0.0.1` เท่านั้น รายละเอียดทั้งหมดอยู่ที่ [SECURITY.md](./SECURITY.md)

---

<div align="center">

<img src="docs/assets/caveman-logo-banner.png" alt="Caveman" width="720">

# why many token when few do trick

**Caveman ทำให้ AI agent พูดน้อยลงและอ่านน้อยลง โค้ดยังเป๊ะ สมองยังใหญ่**

<a href="https://github.com/JuliusBrussee/caveman/stargazers"><img src="https://img.shields.io/github/stars/JuliusBrussee/caveman?style=flat-square&color=F0A63C&label=stars" alt="GitHub stars"></a>
<a href="https://www.npmjs.com/package/@caveman-ai/cli"><img src="https://img.shields.io/npm/dm/@caveman-ai/cli?style=flat-square&color=F0A63C&label=cli%20downloads" alt="npm downloads"></a>
<a href="./INSTALL.md"><img src="https://img.shields.io/badge/works_with-30%2B_agents-orange?style=flat-square" alt="30+ agents"></a>
<a href="#license"><img src="https://img.shields.io/badge/license-Apache--2.0-green?style=flat-square" alt="License"></a>

<table>
<tr>
<td align="center" width="25%"><h3>input token ลดลง 33.2%</h3>ทั้ง session<br><sub><a href="#read-less-332-fewer-input-tokens">Claude Code 54 รอบ</a> ตอบถูก 18 จาก 18</sub></td>
<td align="center" width="25%"><h3>ถูกลง 54%</h3>ด้วย Auto คะแนนเท่าเดิม<br><sub><a href="#auto-54-cheaper-same-score">งานโค้ด 85 งาน</a> เทียบ Opus 5.5 ที่ xhigh ผลระหว่างทาง</sub></td>
<td align="center" width="25%"><h3>397 → 76</h3>token ต่อการรัน test หนึ่งครั้ง<br><sub><a href="#blocks-code-mode-script-written-once">Blocks</a> เทียบ <code>| tail -20</code></sub></td>
<td align="center" width="25%"><h3>ถูกลง 1.4 ถึง 2.4 เท่า</h3>เมื่อตอบแบบ caveman<br><sub><a href="https://arxiv.org/abs/2606.24083">Adobe Research</a> แปดโมเดล</sub></td>
</tr>
</table>

ถูกอ้างอิงโดย **[Adobe Research](https://arxiv.org/abs/2606.24083)** · ทดสอบ A/B โดย **[JetBrains](https://blog.jetbrains.com/ai/2026/07/speak-to-ai-agents-like-cavemen-tosave-tokens/)** · ทำใหม่สำหรับ Elasticsearch บน **[Elasticsearch Labs](https://www.elastic.co/search-labs/blog/elastic-caveman-ai-token-reduction)**<br>
**อันดับ 1** บน [Hacker News](https://news.ycombinator.com/item?id=47647455) · **อันดับ 1** บน GitHub Trending · *"No way this actually works."* [ThePrimeagen](https://www.youtube.com/watch?v=L29q2LRiMRc)

**[ติดตั้ง](#install) · [หกก้อนหิน](#six-rocks-one-install) · [หลักฐาน](#proof) · [พูดน้อยลง](#say-less-the-caveman-voice) · [อ่านน้อยลง](#read-less-332-fewer-input-tokens) · [Auto](#auto-54-cheaper-same-score) · [Blocks](#blocks-code-mode-script-written-once) · [คำสั่ง](#commands) · [Caveman Cloud](#caveman-cloud)**

</div>

---

<table>
<tr>
<th width="50%">เอเจนต์ปกติ · 63 token</th>
<th width="50%"><img src="docs/assets/dancing-rock.svg" width="18" height="18" alt=""> เอเจนต์ caveman · 20 token</th>
</tr>
<tr>
<td valign="top">

> The reason your React component is re-rendering is likely because you're creating a new object reference on each render cycle. When you pass an inline object as a prop, React's shallow comparison sees it as a different object every time, which triggers a re-render. I'd recommend using useMemo to memoize the object.

</td>
<td valign="top">

> New object ref each render, so React re-renders. Wrap the prop in `useMemo`.

</td>
</tr>
</table>

**แก้แบบเดียวกัน จาก 63 token เหลือ 20 สมองยังใหญ่**

เลือกกระบองของคุณ:

| สกิล | คำตอบเดียวกัน | Token |
|---|---|---:|
| `/caveman` | New object ref each render, so React re-renders. Wrap the prop in `useMemo`. | 20 |
| `/ultracave` | Inline object prop, new ref, re-render. `useMemo`. | 14 |
| `/megacave` | 新參照致重繪。`useMemo`。 | **13** |

<sub>นับ token ด้วย tiktoken o200k (ตัวอย่างคงเป็นภาษาต้นฉบับเพราะจำนวน token อ้างอิงข้อความนั้น)</sub>

<a id="install"></a>
## ติดตั้ง

```bash
npx @caveman-ai/cli@latest
```

คำสั่งเดียว ใช้ได้บน Mac, Linux, Windows Caveman จะหาเอเจนต์และ login ของคุณ แล้วแสดงว่าจะเปลี่ยนอะไร กด Enter เสร็จ ต้องใช้ Node.js 22.13 ขึ้นไป

หลังจากนั้น `claude` แบบปกติก็เป็น caveman ไปเลย Codex, Gemini CLI, OpenCode และ[อีกกว่า 30 ตัว](./INSTALL.md) ก็เช่นกัน ทั้งหมดรันบนเครื่องคุณ ใช้ key ของคุณ และ login Claude Pro/Max ของคุณ หินก้อนเดียว จบ

<sub>เคยใช้ caveman ก่อน 4.0? ให้ใส่ <code>@latest</code> ไม่อย่างนั้นสำเนาเก่าในเครื่องจะถูกใช้แทน ตั้งค่าไว้แล้ว? <code>caveman setup</code> เปิดหน้าจอตั้งค่าอีกครั้ง อยากได้แค่คำตอบที่สั้นลง? <a href="#say-less-the-caveman-voice">ติดตั้งแค่สกิล</a></sub>

<a id="six-rocks-one-install"></a>
## หกก้อนหิน ติดตั้งครั้งเดียว

ใหม่ใน 4.0: caveman มีหกส่วน เปิดทั้งหมดหลังติดตั้ง แต่ละส่วนมีสวิตช์ของตัวเอง

| ก้อนหิน | ทำอะไร | ผลวัด |
|---|---|---|
| **[พูดน้อยลง](#say-less-the-caveman-voice)** | เอเจนต์ตอบสั้น โค้ดยังเป๊ะ | 63 → 20 token แก้แบบเดียวกัน |
| **[อ่านน้อยลง](#read-less-332-fewer-input-tokens)** | log, JSON, CSV และ output ของ test ถูกย่อก่อนโมเดลอ่าน | input token ต่อ session ลดลง **33.2%** |
| **[Auto](#auto-54-cheaper-same-score)** · ใหม่ | เลือกโมเดลและระดับ effort ให้แต่ละคำถาม | ถูกกว่า Opus ที่ xhigh **54%** คะแนนเท่าเดิม |
| **[Blocks](#blocks-code-mode-script-written-once)** · ใหม่ | code mode: เอเจนต์เก็บ script ที่เขียนไว้แล้วนำกลับมารันอีก | **397 → 76** token ต่อการรัน test หนึ่งครั้ง |
| **[Waste fixes](#smaller-rocks)** | หาว่า token หายไปไหนแล้วแก้ ใหม่: รักษา prompt cache ให้อุ่นระหว่างที่คุณพัก | ยังไม่ได้วัด |
| **[Browse](#smaller-rocks)** | หน้าเว็บกลับมาแบบย่อแล้ว | หน้าเล็กลง **129.8 เท่า** |

`caveman status` แสดงว่าอะไรเปิดอยู่ `caveman off browse` ปิดทีละส่วน มีแค่ Auto ที่ต้องใช้บัญชี และใช้ฟรี [บันทึกการออกเวอร์ชัน 4.0.0](https://github.com/JuliusBrussee/caveman/releases/tag/v4.0.0)

<a id="proof"></a>
## หลักฐาน

ผลจากภายนอกก่อน ผลของเราอยู่ในแต่ละหัวข้อด้านล่าง ไม่มีการปัดขึ้น แถวที่แพ้ก็ยังแสดงไว้

| ใคร | การทดลอง | ผล |
|---|---|---|
| **[Adobe Research](https://arxiv.org/abs/2606.24083)**, งานวิจัย CAVEWOMAN (อ้างอิง repo นี้) | output แบบ caveman แปดโมเดล ห้าชุดข้อมูล | **ลดค่าใช้จ่าย 1.4 ถึง 2.4 เท่าต่อโมเดล สูงสุด 3 เท่า** |
| **[Elastic](https://www.elastic.co/search-labs/blog/elastic-caveman-ai-token-reduction)**, Elasticsearch Labs | caveman mode ที่ทำใหม่สำหรับ Elasticsearch, MCP จริงแปดสถานการณ์ | **token ในคำตอบลดลง 63.6%** *"Zero information loss."* |
| **[JetBrains](https://blog.jetbrains.com/ai/2026/07/speak-to-ai-agents-like-cavemen-tosave-tokens/)** | งานโค้ดจริง 86 งาน แบบ A/B จับคู่ | **คุณภาพไม่ลดลงอย่างวัดได้** (p = 0.82) output token ลดลง 8.5% |

ข้อค้นพบสองข้อที่หล่อหลอม caveman Adobe พบว่าการย่อ prompt *ของคุณ* ทำให้คำตอบแย่ลง caveman จึงไม่แตะ prompt ของคุณ JetBrains พบว่า session ของเอเจนต์ส่วนใหญ่เป็นโค้ดและการเรียก tool ซึ่งการปรับน้ำเสียงไม่ได้ช่วย caveman จึงเพิ่มก้อนหินที่ย่อสิ่งที่เอเจนต์*อ่าน*และสิ่งที่มัน*รันอยู่บน*

<a id="say-less-the-caveman-voice"></a>
## พูดน้อยลง: น้ำเสียง caveman

**เป็นน้ำเสียง ไม่ใช่ไวยากรณ์ที่พัง ทุกคำตอบมีโครงสร้างเดียวกัน**

| กฎ | ความหมาย |
|---|---|
| **ตอบก่อน** | `[thing] [action] [reason]. [next step].` ไม่ทักทาย ไม่ "let me" ไม่สรุปซ้ำ |
| **หนึ่งประโยคหนึ่งความคิด** | อิงจาก [ASD-STE100](https://www.asd-ste100.org/) ภาษาอังกฤษแบบควบคุมที่ใช้ในคู่มือซ่อมบำรุงเครื่องบิน: ไม่เกิน 20 คำ ใช้ active voice หนึ่งสิ่งใช้หนึ่งคำ |
| **ความหมายไม่หาย** | ตัด article ได้ แต่ *not*, *never*, *no*, *only* ห้ามตัด ตัวเลขและหน่วยต้องตรง |
| **payload ตรงตัว** | โค้ด คำสั่ง path และข้อความ error ไม่ถูกแตะ ตรงทุกตัวอักษร |
| **ไม่แสดงละคร** | ไม่มี "me think" ไม่พูดคั่นระหว่างการเรียก tool ถ้าแบบ caveman ไม่สั้นกว่า ใช้แบบปกติ |
| **รู้ว่าเมื่อไหร่ควรหยุด** | คำเตือนด้านความปลอดภัย การกระทำที่ย้อนกลับไม่ได้ และผู้ใช้ที่สับสน จะได้ประโยคเต็ม แล้วค่อยกลับมาห้วนต่อ |
| **prompt ของคุณยังเป็นของคุณ** | ไม่ถูกเขียนใหม่ [งานวิจัยบอกว่าทำแล้วแย่ลง](#proof) |

คำถามด้าน dev สิบข้อบน claude-opus-5-5:

| คำสั่ง | output token |
|---|---:|
| ไม่มี | 6,983 |
| `Answer concisely.` | 4,334 |
| `/caveman` | 4,119 |
| `/ultracave` | **2,693** |

"Be concise" คือ baseline ที่แท้จริง เพราะโมเดลใหม่รู้จักอยู่แล้ว เมื่อเทียบกับมัน `/caveman` ลดเพิ่มอีก 3% ที่ค่ามัธยฐาน และ `/ultracave` ลดเพิ่มอีก 35% วัดบนกฎของเวอร์ชัน 3.1.0 ยังไม่ได้วัดใหม่ ตัวกฎกิน input ราว 1,160 token และถ้าคุณจ่ายต่อ request (GitHub Copilot) คำตอบที่สั้นลงไม่ได้ช่วยประหยัด [ชุดทดสอบ](./evals/README.md) · [ทุกกรณีที่ caveman แพ้](./docs/HONEST-NUMBERS.md)

<!-- BENCHMARK-TABLE-START -->
<!-- BENCHMARK-TABLE-END -->

**อยากได้แค่ก้อนนี้?** ติดตั้งแค่สกิล ไม่มี proxy:

```bash
npx skills add JuliusBrussee/caveman -g
```

<a href="https://skills.sh/JuliusBrussee/caveman"><img src="https://skills.sh/b/JuliusBrussee/caveman" alt="skills.sh"></a>

พิมพ์ `/caveman` (`$caveman` ใน Codex) ถ้ามันไม่เริ่มเอง พูด `stop caveman` เพื่อกลับเป็นปกติ

<details>
<summary><strong>วิธีติดตั้งอื่น</strong>: แอป Claude และมือถือ, Claude Code plugin, Gemini, ทุกเอเจนต์พร้อมกัน, Windows, ถอนการติดตั้ง</summary>

<br>

ใช้ Claude บนเว็บ แอปมือถือ หรือ Cowork? ไม่มี terminal ให้เพิ่ม caveman เข้าบัญชี Claude ครั้งเดียวที่ Customize > Plugins: [ขั้นตอน](./INSTALL.md#claude-apps-claudeai-desktop-mobile-cowork) ยังไม่ได้ทดสอบครบทุกขั้น

```bash
# Claude Code plugin, auto-starts every interactive session, subagents too
claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman

# Gemini CLI
gemini extensions install https://github.com/JuliusBrussee/caveman

# Every agent on your machine at once, plus the Claude Code statusline badge (Node.js 22.13+)
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/v4.0.1/install.sh | bash
```

อยู่ใน Claude Code อยู่แล้ว? ก้อนเดียวกันแบบ slash command พิมพ์ตรงช่องที่คุยกับ Claude:

```text
/plugin marketplace add JuliusBrussee/caveman
/plugin install caveman@caveman
```

Windows, PowerShell 5.1 ขึ้นไป:

```powershell
irm https://raw.githubusercontent.com/JuliusBrussee/caveman/v4.0.1/install.ps1 | iex
```

npm 12 ขึ้นไปบล็อกการติดตั้งจาก git คำสั่งบรรทัดเดียวด้านบนจัดการเองตั้งแต่ v3.2.0 คำสั่งเก่าที่ pin ไว้ที่ v3.1.0 หรือเก่ากว่ายังจะล้มเหลว ให้ใช้คำสั่งด้านบน หรือคำสั่งนี้:
`npx --allow-git=root -y github:JuliusBrussee/caveman#v4.0.1`

เปลี่ยนใจ: `npx -y github:JuliusBrussee/caveman -- --uninstall` (บน npm 12 ขึ้นไป ให้เพิ่ม `--allow-git=root` ด้วย)

ติดตั้งแค่สกิล? `npx skills remove JuliusBrussee/caveman -g` เอาออก

ติดตั้งแล้วพัง? เปิดเอเจนต์ใน repo นี้แล้วพูดว่า *"Read CLAUDE.md and INSTALL.md, install caveman for me."* ให้เอเจนต์ซ่อมสมองตัวเอง

</details>

<a id="read-less-332-fewer-input-tokens"></a>
## อ่านน้อยลง: input token ลดลง 33.2%

**น้ำเสียงย่อสิ่งที่เอเจนต์พูด ส่วนนี้ย่อสิ่งที่มันอ่าน คำตอบเหมือนเดิม: ถูก 18 จาก 18**

| ชนิดไฟล์ | ไฟล์ผ่าน caveman | ไฟล์ประหยัด | ทั้ง session ของ Claude Code, 3 รอบ | session ประหยัด |
|---|---:|---:|---:|---:|
| CSV | 28,041 → **314** | **98.9%** | 165,823 → 74,484 | **55.1%** |
| Logs | 22,810 → **348** | **98.5%** | 148,807 → 74,068 | **50.2%** |
| YAML | 20,447 → **178** | **99.1%** | 132,124 → 71,027 | **46.2%** |
| Test output | 18,806 → **203** | **98.9%** | 150,377 → 108,514 | **27.8%** |
| JSON | 18,837 → **281** | **98.5%** | 147,975 → 108,939 | **26.4%** |
| HTML | 21,670 → 21,670 | ยังไม่มี | 140,687 → 154,641 | แย่ลง 9.9% |
| **ทั้งหกชนิด** | 130,611 → 22,994 | 82.4% | **885,793 → 591,673** | **33.2%** |

*ไฟล์* คือไฟล์ทดสอบแต่ละไฟล์ที่ผ่านตัวย่อเวอร์ชันปัจจุบันอย่างเดียว *session* คือการรันเอเจนต์ทั้งหมด ซึ่งมี system prompt และ tool ติดไปด้วย จึงลดได้น้อยกว่า ส่วนที่ต้องพูดตรง ๆ: การรัน session มาจากเดือนสิงหาคม 2026 บน engine รุ่นเก่า HTML ยังไม่มีตัวย่อจึงแพ้ และไฟล์ทดสอบแต่ละไฟล์ซ่อนข้อมูลหนึ่งรายการไว้ในข้อมูลรก 61 ถึง 72 KB ของคุณอาจต่างออกไป Headroom บนชุดทดสอบเดียวกัน: ถูก 15 จาก 18 token ลดลง 6.7% [วิธีวัด](./docs/WRAP-BENCHMARK.md#per-file-compression)

ต้นฉบับทุกไฟล์ยังอยู่บนดิสก์ของคุณ เอเจนต์ดึงกลับมาได้ทุกเมื่อ

<a id="auto-54-cheaper-same-score"></a>
## Auto: ถูกลง 54% คะแนนเท่าเดิม

**โมเดลใหม่ในตัวเลือกโมเดลของเอเจนต์ เลือก Auto แล้ว caveman จะเลือกโมเดลและ effort ให้แต่ละคำถาม คำถามยากใช้สมองใหญ่ คำถามง่ายประหยัดหิน**

| การตั้งค่า | งานที่แก้ได้ | ค่าใช้จ่ายต่อครั้ง | เวลามัธยฐาน |
|---|---:|---:|---:|
| Opus 5.5, effort xhigh ทุกคำถาม | 44.3% | $7.83 | 35.2 นาที |
| **Auto**, เฉพาะโมเดล Claude | **43.7%** | **$3.59** | **15.9 นาที** |
| **Auto**, รวม OpenAI และโมเดล open | 42.9% | $3.47 | 16.7 นาที |

Auto มีค่าใช้จ่าย 0.46 เท่าของ Opus 5.5 ที่ xhigh คือประหยัด 54% ในเวลาไม่ถึงครึ่ง งานโค้ดจริง 85 งานจาก SWE-Interact และ SWE-Together ลองงานละครั้ง ส่วนที่ต้องพูดตรง ๆ: รันไปได้แค่ครึ่งเดียว ช่องว่างคะแนน 0.5 จุดเล็กเกินกว่าจะแยกได้ที่ขนาดนี้ (±7) และที่ประหยัดส่วนใหญ่มาจาก Auto ลด effort ในคำถามง่าย ใช้ Opus ที่ medium อยู่แล้ว? คาดว่าจะประหยัดน้อยกว่านี้ ยังไม่ได้วัด [ตารางเต็มและข้อจำกัด](./docs/AUTO-BENCHMARK.md)

```bash
caveman login                  # free account. Auto shows up in the model picker
caveman providers add openai   # optional: give Auto more models, on your own key
```

ใช้ได้ใน Claude Code, OpenCode และ Codex ที่ login ด้วย ChatGPT โดยใช้ API key, Claude Pro/Max หรือ ChatGPT โมเดลอื่นที่คุณเลือกเองจะรันตามที่เลือก ไม่ได้ login: ไม่มี Auto ไม่มีอะไรถูกส่งออกไป [Auto ส่งอะไรบ้าง](#privacy)

<a id="blocks-code-mode-script-written-once"></a>
## Blocks: code mode เขียน script ครั้งเดียว

**skills.sh สำหรับ code mode** code mode คือการที่เอเจนต์เขียน script แทนการเรียก tool ทีละครั้ง ([Cloudflare](https://blog.cloudflare.com/code-mode/), [Anthropic](https://www.anthropic.com/engineering/code-execution-with-mcp)) ปัญหาคือเอเจนต์เขียน script เดิมทุก session ทิ้ง แล้วเขียนใหม่ Blocks เก็บมันไว้ใน repo ของคุณ ตรวจทุก pull request แล้วส่งคืนให้ใช้

| Input | ดิบ | สิ่งที่เอเจนต์พิมพ์ตอนนี้ | Block |
|---|---:|---:|---:|
| `go test -v ./...`, 326 tests | 10,561 | 397 · `\| tail -20` | **76** · `test-summary` |
| ไฟล์ JSON 1.4 MB | 251,893 | 236 · heredoc ที่เขียนเอง | **227** · `json-peek` |
| ไฟล์ Go 366 บรรทัด | 3,111 | **250** · `grep -n` | 489 · `grep-defs` |

คือ token ที่เอเจนต์อ่านกลับ ในหนึ่งสัปดาห์ เอเจนต์บนเครื่องเดียวเขียน script เดิม [394 ครั้ง](https://github.com/caveman-ai/blocks#one-script-written-394-times-in-a-week) [Purdue](https://arxiv.org/abs/2609.30725) วัดว่านิสัยนี้กินได้ถึง 9.57% ของค่าใช้จ่ายต่องาน `grep-defs` แพ้ grep เปล่า ๆ แถวนี้ก็ยังอยู่ [วิธีวัด](https://github.com/caveman-ai/blocks#blocks-against-what-agents-type-now)

มาพร้อม caveman มีแปด block พร้อมใช้: `json-peek` · `jsonl-stats` · `test-summary` · `first-error` · `wait-for` · `grep-defs` · `http-json` · `replace-in-file` เมื่อเอเจนต์เริ่มพิมพ์ script ที่มี block ครอบคลุมอยู่แล้ว มันจะได้ข้อความหนึ่งบรรทัด: ใช้ block ไม่เคยปฏิเสธหรือเขียนคำสั่งใหม่

```bash
caveman-blocks scan    # what your agents retyped this month. Script text never leaves your machine
caveman-blocks init    # rules and block index into this repo's AGENTS.md
```

ยังเป็น pre-release (v0.1.0-rc.5) รองรับแค่ Python ยังไม่มี sandbox มี repo และดาวของตัวเอง: **[caveman-ai/blocks](https://github.com/caveman-ai/blocks)**

<a id="smaller-rocks"></a>
## ก้อนหินที่เล็กกว่า

| ก้อนหิน | ทำอะไร | ผลวัด |
|---|---|---|
| `caveman learn` | จัดอันดับว่า token หายไปไหน จากประวัติเอเจนต์ที่มีอยู่บนดิสก์ `caveman learn implement` แก้ทีละ diff เมื่อคุณตอบตกลงเท่านั้น | ยังไม่ได้วัด |
| Warm cache · ใหม่ | พอคุณลุกไป provider จะลืม session ทำให้คำถามถัดไปจ่ายราคาเต็ม Caveman รักษา prompt cache ของ Anthropic ให้อุ่นระหว่างที่คุณพัก เฉพาะเมื่อประวัติของคุณบอกว่าจะกลับมาทัน ทุกครั้งที่ warm ดูได้ใน `caveman stats` | ยังไม่ได้วัด |
| `caveman browse <url>` | หน้าเว็บแบบย่อสำหรับเอเจนต์ | **121 token แทน 15,704** สำหรับ Playwright snapshot ของตาราง 200 แถว ฟอร์มเล็ก ๆ แพ้ 2.3 เท่า [Bench](./browse/BENCHMARK.md) |
| `/caveman-compress <file>` | ย่อไฟล์ memory อย่าง `CLAUDE.md` และเก็บ backup ไว้ | **4,138 token แทน 6,198** จากห้าไฟล์ ไฟล์ละ 22.8% ถึง 49.1% heading, code block และ path ครบทุกอัน [Bench](./skills/caveman-compress/README.md#benchmarks) |
| Middleware | ย่อแบบเดียวกันภายใน Vercel AI SDK, LangChain, OpenAI หรือ Anthropic call ที่คุณใช้อยู่ [TypeScript](./packages/middleware/typescript/README.md) · [Python](./packages/middleware/python/README.md) · [ทุก framework](https://docs.caveman.so/caveman/middleware) · [container เดียวสำหรับทั้งทีม](docs/technical/deploy.md) | ยังไม่ได้วัด |

<p align="center">
  <img src="docs/assets/learn-report.png" alt="Caveman Learn report: a summary and savings cards on the left; the biggest places tokens go, with one fix opened, and a chart of how full sessions get on the right" width="900">
</p>

<a id="commands"></a>
## คำสั่ง

ใน terminal:

```bash
caveman claude                # start an agent on caveman: codex · gemini · opencode · aider · kilo · qwen · hermes · openclaw · pi
caveman status                # what is on, which agents it reaches, one next step
caveman on browse             # switch one rock on or off: output · input · waste-fixes · routing · scripts · browse
caveman login                 # free account, turns on Auto
caveman learn                 # where your tokens go
caveman trial -- claude       # A/B a real session on your own work
caveman shrink -- pnpm test   # compress noisy command output
caveman convert --dry-run     # pixel mode: skills the model reads as images
caveman stats                 # your token history
caveman doctor                # one problem per line, with its fix
```

ในเอเจนต์:

| คำสั่ง | ทำอะไร |
|---|---|
| `/caveman` · `/ultracave` · `/megacave` | น้ำเสียง, เสียงคำราม, และ 文言文 `/caveman status` แสดงโหมด `/caveman off` ปิด |
| `/caveman-commit` | Conventional Commit บรรทัดเดียว |
| `/caveman-review` | หนึ่งข้อค้นพบต่อบรรทัด: `L42: 🔴 null deref. Guard it.` |
| `/caveman-compress <file>` | ย่อไฟล์ memory และ backup ต้นฉบับ |
| `/caveman-stats` | การใช้ token จริงของ session Claude Code นี้ |
| `/caveman-help` | ทุกโหมดและคำสั่งในหน้าจอเดียว |
| `cavecrew` | subagent ที่หา แก้ และรีวิวโค้ด แล้วรายงานกลับแบบ caveman |
| `investigate-first` · `lean-build` · `surgical-patch` · `safe-refactor` · `migration` · `verify-and-stop` | รูปแบบการทำงานที่เขียนโค้ดน้อยลง เอเจนต์จะหยิบมาใช้เองเมื่องานเข้าเงื่อนไข |
| `caveman-setup` · `caveman-discover` · `caveman-learn` · `caveman-manage` · `caveman-optimize` · `caveman-explore` · `caveman-evidence-review` | ควบคุม proxy จากในเอเจนต์ |

<a id="caveman-cloud"></a>
## Caveman Cloud

**ทุกอย่างด้านบนใช้กับเอเจนต์เขียนโค้ดที่คุณใช้ Caveman Cloud ใช้กับเอเจนต์ที่คุณสร้าง**

คุณส่งมอบเอเจนต์ ทุกการรันมีค่าใช้จ่าย มันดีไหม? ถูกไหม? การเปลี่ยนแปลงไหนทำให้แย่ลง? Cloud ตอบได้

| สิ่งที่ Cloud ทำ | สิ่งที่คุณได้ |
|---|---|
| **Observability** | ทุกการรันถูก trace ไปถึงงานและค่าใช้จ่าย ตั้งค่าตัวเองจาก repo, key และ log หรือ OpenTelemetry ที่คุณมีอยู่แล้ว |
| **Evals** | ให้คะแนนคุณภาพคำตอบ บนงานของคุณเอง จาก traffic จริง |
| **Autopilot** | เสนอการเปลี่ยนแปลงที่ถูกกว่า ทดสอบบนงานที่บันทึกไว้ และปล่อยเฉพาะเมื่อ eval บอกว่าคำตอบยังดีเท่าเดิม คุณเป็นคนอนุมัติ pull request |
| **Proof** | ทุกตัวเลขบอกว่าวัดจริง อนุมาน หรือยืนยันแล้ว การประหยัดนับเมื่อ traffic จริงแสดงผลเท่านั้น |

<p align="center">
<a href="https://app.caveman.so/signup"><b>สมัครฟรี</b></a> &nbsp;·&nbsp; <a href="https://caveman.so/demo">ลองเดโม</a> &nbsp;·&nbsp; <a href="https://cal.com/caveman/chat">นัดคุย</a> &nbsp;·&nbsp; <a href="https://docs.caveman.so">เอกสาร</a>
</p>

<a id="in-the-wild"></a>
## ในโลกจริง

<a href="https://www.youtube.com/watch?v=L29q2LRiMRc"><img src="https://img.youtube.com/vi/L29q2LRiMRc/hqdefault.jpg" alt="ThePrimeagen reacts to Caveman: No way this actually works" width="340" align="right"></a>

**ThePrimeagen**: *"No way this actually works."* [ดู](https://www.youtube.com/watch?v=L29q2LRiMRc)

**Adobe Research**: [CAVEWOMAN](https://arxiv.org/abs/2606.24083), arXiv, มิถุนายน 2026

**JetBrains**: *"It is fun, and it costs you nothing measurable in quality."* [อ่าน](https://blog.jetbrains.com/ai/2026/07/speak-to-ai-agents-like-cavemen-tosave-tokens/)

**Elastic**: [elastic-caveman](https://www.elastic.co/search-labs/blog/elastic-caveman-ai-token-reduction) บน Elasticsearch Labs, เมษายน 2026

**Hacker News**: [อันดับ 1, 904 คะแนน](https://news.ycombinator.com/item?id=47647455)

**GitHub Trending** อันดับ 1 รวมทุกภาษา กรกฎาคม 2026 · **[Trendshift](https://trendshift.io/repositories/25391)** repo อันดับ 1 ของวัน เมษายน 2026 · **[Product Hunt](https://www.producthunt.com/products/caveman)** อันดับ 8 ของวัน

เริ่มจากมุกตลกในเดือนเมษายน 2026 ตอนนี้ดาวเกิน 100,000 แล้ว มุกกลายเป็นเรื่องจริงจัง แต่น้ำเสียงไม่เปลี่ยน

<br clear="right">

[![Star History Chart](./docs/assets/star-history.png)](https://star-history.com/#JuliusBrussee/caveman&Date)

<a id="privacy"></a>
## ความเป็นส่วนตัว

- **สกิล** รันบนเครื่องคุณและไม่ส่งอะไรออกไป ยกเว้นข้อเดียว: `/caveman-compress` ส่งไฟล์ที่คุณย่อไปยัง model provider ที่คุณตั้งไว้
- **CLI** ส่งสถิติการใช้งานเป็นค่าเริ่มต้น: คำสั่งที่รัน จำนวน token คำสั่งและจำนวนการใช้ caveman-blocks, install ID แบบสุ่ม, OS และ IP ไม่ส่ง prompt โค้ด path ของไฟล์ หรือ script ที่คุณเขียน มีคนดูแลโปรเจกต์นี้คนเดียวแบบไม่คิดเงิน และสถิติเหล่านี้บอกว่าควรสร้างอะไรต่อ ปิดถาวร รวม Blocks ด้วย: `caveman telemetry off` หรือ `DO_NOT_TRACK=1`
- **Auto** เฉพาะเมื่อคุณ login และเลือกมัน: แต่ละคำถามจะส่งคำถามล่าสุดของคุณไปให้ Caveman Cloud (พร้อมสิ่งที่เอเจนต์แนบไป เช่น CLAUDE.md, memory หรือไฟล์ที่ @ ถึง) คำถามก่อนหน้า และท้ายคำตอบล่าสุดของเอเจนต์ รวมถึงชื่อ tool, effort, header ของเอเจนต์บางตัว และจำนวน token ของ request ก่อนหน้า ในแผน Free ทาง Caveman อาจเก็บไว้เพื่อปรับปรุง routing `caveman off routing` ปิดได้
- **request ไปที่ไหน:** จากเครื่องคุณไปยัง provider ของคุณ หรือ provider อื่นที่คุณเพิ่มด้วย `caveman providers add` โดยใช้ key ของคุณ มีแค่ request ที่ถูก route ไปโมเดลของ Caveman Cloud เท่านั้นที่ผ่าน Caveman Cloud ทั้งก้อน (system prompt, tool result, โค้ด) ใช้ key ที่เก็บไว้ในโปรเจกต์ Caveman และคิดเงินกับโปรเจกต์นั้น `caveman providers cloud off` ปิดได้

รายการทั้งหมด และวิธีลบ telemetry ที่ส่งไปแล้ว: [SECURITY.md](./SECURITY.md)

<a id="license"></a>
## สัญญาอนุญาต

[Apache-2.0](./LICENSE) ทั้ง repo อ่าน fork ส่งมอบ หรือ host ได้ ฟรีเหมือนแมมมอธบนทุ่งโล่ง รุ่นเก่าและประกาศของบุคคลที่สาม: [LICENSING.md](./LICENSING.md) "Caveman" และโลโก้รูปหินเป็นเครื่องหมายการค้าของ Julius Brussee

<a id="cite"></a>
## การอ้างอิง

```bibtex
@software{brussee2026caveman,
  author = {Brussee, Julius},
  title  = {Caveman: why many token when few do trick},
  year   = {2026},
  url    = {https://github.com/JuliusBrussee/caveman}
}
```

---

<div align="center">

🪨 **Caveman ช่วยคุณประหยัด token กดดาวไม่เสียอะไร แลกกันยุติธรรม**

<sub>
<a href="./docs/README.md">เอกสาร</a> ·
<a href="./INSTALL.md">ตารางการติดตั้ง</a> ·
<a href="./docs/HONEST-NUMBERS.md">ตัวเลขตามจริง</a> ·
<a href="./CONTRIBUTING.md">ร่วมพัฒนา</a> ·
<a href="https://app.caveman.so/signup">Caveman Cloud</a> ·
<a href="https://github.com/JuliusBrussee/caveman/issues">Issues</a>
</sub>

</div>
