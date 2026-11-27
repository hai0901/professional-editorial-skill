# Vietnamese professional writing

Target: text that a competent Vietnamese engineer, analyst or manager would write for colleagues. It should not read like a translation from English or like a developer's notes. Mixing English and Vietnamese is fine when it matches how practitioners actually talk. Do not aim for a fixed ratio.

## Choosing a term

Work through these in order for each technical term:

1. **Is it an identifier?** This covers code names, function names, fields, status values, file names, product or model names (`replay()`, `OPTIMAL`, `sort_key`, `CP-SAT`). Keep it verbatim, formatted as code, and make the sentence around it meaningful: "Cả ba bước tối ưu đều trả về trạng thái `OPTIMAL`", not "Cả ba tầng OPTIMAL".
2. **Do practitioners in this field use a Vietnamese term?** Check the project's documents, glossary and standards first. Use that term ("đầu vào", "tồn kho", "ràng buộc", "trung vị", "triển khai").
3. **Is the English term the working term in the field?** Keep it (API, benchmark, pipeline, P50, deploy, commit, dashboard). For a non-specialist audience, add a short Vietnamese gloss at first use.
4. **Neither?** Describe the concept in Vietnamese and put the English term in parentheses at first use: "tập kiểm tra tách theo thời gian (time-based holdout)".

Do not translate glue words and leave the grammar in English ("P50 nếu n≥30, else mô hình line"). Do not translate an identifier into prose and lose the link to the implementation.

## Patterns to fix

Each row gives the signal to look for, an example, and a fix. The examples illustrate patterns. They are not replacement rules: always check the meaning in context.

| Pattern | Signal | Before | After |
|---|---|---|---|
| Calque (word-for-word translation) | The phrase is a literal rendering of an English technical term and a practitioner would not say it | "láng giềng của một lượt" (neighbour); "hạt giống của A" (seed); "ảnh chụp 10:00" (snapshot); "tập giữ lại" (holdout); "chữ ký route" (signature); "vật lý của bin" (physics) | "phương án lân cận, tạo bằng cách điều chỉnh một lượt"; "phương án khởi tạo do A tạo ra"; "trạng thái lúc 10:00"; "tập kiểm tra"; "mã nhận diện route"; "cân bằng khối lượng của bin" |
| Note-style fragment | No subject or verb; reads like a bullet from a developer's notes | "Hiệu chỉnh bằng dữ liệu nghiên cứu." / "Lúc 10:00: 100 ứng viên, 0,74 s." | "Tham số được hiệu chỉnh bằng dữ liệu nghiên cứu." / "Trong lần tính lúc 10:00, bộ giải xét 100 ứng viên và hoàn thành sau 0,74 giây." |
| Spoken register and internal slang | cái, thì, lọt, ghim, kẹt, đỡ, chấm, "tính cái gì" | "giữ 3 cái có sort_key nhỏ nhất"; "không có gì lọt giữa hai mốc"; "rồi ghim lại" | "giữ 3 phương án xếp hạng tốt nhất"; "các thay đổi được tính tại thời điểm xảy ra sự kiện"; "rồi lưu làm bản tham chiếu" |
| Personified software | Software "sees", "knows", "believes" or "decides" | "thứ duy nhất solver nhìn thấy"; "lõi không biết mẻ"; "engine tin lượt sẽ chạy tiếp" | "dữ liệu đầu vào duy nhất của solver"; "bộ tối ưu không xử lý mẻ"; "engine dự kiến lượt sẽ tiếp tục" |
| Ambiguous "thật / thực tế" | Used for simulated, synthetic or test data | "Ví dụ thật E1"; cột "Thực tế" trong bảng mô phỏng | "Ví dụ trong kịch bản E1"; "Thực tế (mô phỏng)" |
| Nominalization chains | việc, sự, tiến hành, thực hiện, mang tính | "tiến hành thực hiện việc đánh giá" | "đánh giá" |
| Redundant passive | được/bị where the agent is known | "Việc kiểm tra được thực hiện bởi hệ thống" | "Hệ thống kiểm tra …" |
| Noun stacks | Five or more nouns in a row | "hệ thống quản lý giám sát vận hành tồn kho nguyên liệu" | "hệ thống giám sát tồn kho nguyên liệu trong vận hành" (or split the sentence) |
| Inflated Sino-Vietnamese | Grand words for ordinary facts | "mang tính đột phá", "hiện thực hóa", "tối ưu vượt trội", "nâng tầm" | Say what changed and by how much |
| Empty openers | Phrases that announce instead of saying | "Có thể thấy rằng", "Điều đáng chú ý là", "Nhìn chung", "Như đã đề cập ở trên" | Delete them and state the point |
| Undefined abbreviation | An abbreviation first appears without its full form | "NL m" | "nguyên liệu (NL) m" at first use |
| Doubled word from a careless edit | Two identical words in a row | "biết giờ chạy lại lại tệ hơn" | "biết trước giờ chạy lại cho kết quả tệ hơn" |
| Personal pronouns in formal documents | tôi, anh, em, mình, chúng ta in reports or specifications | "chưa được anh duyệt"; "lúc trước tôi nói …" | "chưa được người phụ trách duyệt"; "đính chính giải thích trước đây: …" (emails and chat may use pronouns) |

## Punctuation and number formats

- No space before , . : ; ? ! and one space after. Use “ ” for quotation marks in prose. Use straight quotes only inside code.
- Numbers: Vietnamese usage is a comma for decimals and a dot or a thin space for thousands (`1.234,5` or `1 234,5`). Pick one style per document. **In proofread mode, do not reformat numbers.** Flag inconsistent formats instead, because changing a number's format can change its value for readers.
- Units: be consistent about the space before units and % (`5 s`, `80 %` or `80%`). Follow the project convention if there is one.
- Time and date: `10:00`, `16/10/2026`. Do not mix in `10h00` or `10.00` within the same document.

## Register by genre

| Genre | Register |
|---|---|
| Technical report, specification | Neutral and impersonal; full sentences; define terms once |
| Executive memo, management report | Lead with the conclusion and the decision needed; minimal jargon; numbers with context |
| Email, Teams message | Direct and polite; lead with the request; pronouns are acceptable; short paragraphs |
| Slide text | Titles state the message, not the topic; fragments are acceptable on slides but not in the speaker notes or the report |
| Operator-facing UI text | Short imperative or status phrases; the plant's own vocabulary; no internal codes without explanation |
