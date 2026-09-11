# K4 — Ngày 1: Bài Tập & Phản Ánh
## Khám Phá LLM API | Phiếu Thực Hành

**Thời lượng:** 4 tiếng
**Cách làm:** Trả lời từng câu ngay sau khi hoàn thành block tương ứng —
đừng để dồn hết về cuối buổi. Thay dòng `*Câu trả lời của bạn*` bằng câu
trả lời thật (chấm tự động sẽ đếm số câu đã trả lời).

---

## Block 1 — API Cơ Bản (trả lời sau Checkpoint 1)

### Câu 1.1 — Độ nhạy của temperature
Gọi `call_openai` với temperature 0.0, 0.5, 1.0 và 1.5 dùng prompt
**"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> Khi temperature tăng từ 0.0 lên 1.5, câu trả lời có xu hướng đa dạng hơn về nội dung và cách diễn đạt. Ở temperature thấp, phản hồi thường ổn định và dễ dự đoán hơn, trong khi temperature cao tạo ra các câu trả lời ngẫu nhiên và sáng tạo hơn.

### Câu 1.2 — Chọn temperature cho sản phẩm
**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Tùy thuộc vào yêu cầu cũng như doanh nghiệp nhưng bản thân Mình sẽ để dưới 0.5 để có độ chính xác cao nhất

### Câu 1.3 — Đánh đổi chi phí
Kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người gọi API 3 lần,
mỗi lần trung bình ~350 token đầu ra.

**Ước tính GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này? Nêu một
trường hợp GPT-4o xứng đáng với chi phí và một trường hợp nên dùng mini:**
> GPT-4o đắt hơn GPT-4o-mini khoảng 16,7 lần

---

## Block 2 — System Prompt & Token (trả lời sau Checkpoint 2)

### Câu 2.1 — Sức mạnh của persona
Gọi `chat_with_system_prompt` hai lần với cùng câu hỏi
**"Giải thích blockchain là gì?"** nhưng hai system prompt khác nhau:
- "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi."
- "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật."

**Hai phản hồi khác nhau như thế nào (độ dài, từ vựng, ví dụ)? System prompt
ảnh hưởng đến hành vi model ra sao?** (3–4 câu)
> nếu là câu bạn là giáo viên tiểu học thì output của nó sẽ giải thích đơn giản, đưa ví dụ dễ hiểu cũng như minh họa đời thường. Còn nếu là một chuyên gia tài chính thì câu trả lời lại phân tích chuyên sâu hơn, có tình hình thực tế thế giới cũng như lượng cung cầu, và đưa ra nhiều thuật ngữ chuyên ngành

### Câu 2.2 — tiktoken vs đếm từ
Chọn một đoạn văn tiếng Việt ~100 từ. So sánh số token theo `count_tokens`
(tiktoken) với ước lượng `số từ / 0.75` mà Part 1 đã dùng.

**Hai con số chênh nhau bao nhiêu phần trăm? Vì sao tiếng Việt thường tốn
nhiều token hơn tiếng Anh cùng độ dài?**
> thường thì tiếng việt nhiều token hơn vì nó có dấu và cấu trúc ký tự/chuỗi từ khác tiếng Anh vì tokenizer có thể phải tách một từ tiếng Việt thành nhiều token hơn. Chênh nhau khoảng 20%

---

## Block 3 — Streaming & Độ Bền (trả lời sau Checkpoint 3)

### Câu 3.1 — Trải nghiệm người dùng với streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì
non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming quan trọng nhất khi người dùng cần nhận phản hồi ngay từng phần thay vì phải chờ toàn bộ câu trả lời được tạo xong. Nó giúp giảm cảm giác phải chờ và làm trải nghiệm tương tác tốt hơn. Ngược lại, non-streaming phù hợp hơn khi cần nhận toàn bộ kết quả một lần để xử lý tiếp, lưu dữ liệu hoặc khi câu trả lời ngắn và thời gian chờ không đáng kể.

### Câu 3.2 — Vì sao backoff theo cấp số nhân?
**So với delay cố định (ví dụ luôn chờ 1 giây), exponential backoff có lợi
thế gì khi API bị quá tải? Điều gì xảy ra nếu hàng nghìn client cùng retry
với delay cố định giống nhau?**
> Exponential backoff giúp giảm áp lực lên API khi hệ thống đang quá tải bằng cách tăng dần thời gian chờ giữa các lần retry. Nếu hàng nghìn client cùng retry với delay cố định, chẳng hạn đều chờ đúng 1 giây, chúng có thể gửi request lại cùng một thời điểm, tạo thành một đợt tải lớn mới và khiến API càng quá tải. Exponential backoff giúp các request được phân tán hơn theo thời gian, từ đó tăng khả năng hệ thống phục hồi.

---

## Block 4 — Mini-Project (trả lời sau Checkpoint 4)

### Câu 4.1 — Thiết kế persona
**Bạn chọn persona gì cho trợ lý của mình? Viết lại system prompt đó và giải
thích 1–2 lựa chọn từ ngữ quan trọng trong prompt (ví dụ: vì sao yêu cầu
"trả lời ngắn gọn", vì sao chỉ định ngôn ngữ...):**
> Persona mình chọn: Trợ lý phát triển bản thân, thân thiện và đồng hành với người dùng trong việc cải thiện sức khỏe tinh thần, thể chất và thói quen sống. System prompt: Bạn là một trợ lý phát triển bản thân thân thiện và đồng cảm. Bạn hỗ trợ người dùng cải thiện sức khỏe tinh thần, sức khỏe thể chất, thói quen và chất lượng cuộc sống. Hãy đưa ra lời khuyên thực tế, dễ áp dụng và không phán xét. Ưu tiên trả lời ngắn gọn, rõ ràng và bằng tiếng Việt. Cụm “thân thiện và đồng cảm” giúp trợ lý có cách giao tiếp nhẹ nhàng, phù hợp với những chủ đề nhạy cảm như tâm lý và cảm xúc. Cụm “thực tế, dễ áp dụng” giúp câu trả lời không chỉ đưa ra lý thuyết mà còn hướng người dùng đến những hành động cụ thể có thể thực hiện trong cuộc sống.

### Câu 4.2 — Hạn chế & cải thiện
**Trợ lý của bạn hiện có hạn chế lớn nhất là gì (ví dụ: history chỉ 3 lượt,
không có bộ nhớ dài hạn, không kiểm duyệt nội dung...)? Đề xuất một cải
thiện cụ thể và mô tả ngắn cách triển khai:**
> Không có cảm xúc hay vẫn mang văn phong Ai khi mình cần giúp đỡ và chưa có khả năng đánh giá chính xác tình trạng của người dùng. Một cải thiện cụ thể là xây dựng hệ thống cá nhân hóa, cho phép trợ lý thu thập mục tiêu, thói quen và phản hồi của người dùng để đưa ra lời khuyên phù hợp hơn theo từng trường hợp.

---

## Danh Sách Kiểm Tra Nộp Bài

- [ ] `python grade.py` — xem điểm tự động, mục tiêu ≥ 75/100
- [ ] Cả 4 checkpoint pytest đều pass
- [ ] Tất cả 9 câu trong file này đã được trả lời
- [ ] Đã copy bài làm vào folder `solution/`, push lên fork và dán link trên trang bài Lab ở VLearn trước 23:59 ngày 11/09/2026
