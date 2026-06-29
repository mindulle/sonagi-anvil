export async function onRequestPost(context) {
    try {
        // 프론트엔드에서 보낸 JSON 데이터 파싱
        const data = await context.request.json();
        const { questionId, timeRemaining, q1, q2, q3 } = data;

        // D1 데이터베이스(바인딩된 이름: DB)에 INSERT
        const stmt = context.env.DB.prepare(
            `INSERT INTO evaluations (question_id, time_remaining, logic_bug_feedback, complexity_feedback, final_feedback) 
             VALUES (?, ?, ?, ?, ?)`
        ).bind(questionId, timeRemaining, q1, q2, q3);
        
        await stmt.run();

        return new Response(JSON.stringify({ success: true, message: "Record saved successfully" }), {
            headers: { "Content-Type": "application/json" }
        });
    } catch (err) {
        return new Response(JSON.stringify({ success: false, error: err.message }), {
            status: 500,
            headers: { "Content-Type": "application/json" }
        });
    }
}
