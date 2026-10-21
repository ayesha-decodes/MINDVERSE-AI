# Science and methodology

MindVerse AI is an educational game experience, not a medical or psychological assessment.

- **Reaction time:** measured as response timestamp minus target onset using `performance.now()`. Display latency, input device, browser scheduling and anticipation affect results.
- **Memory Matrix:** records the user's tile selections against the generated sequence. This is a custom game mechanic, not a validated memory test.
- **Focus Flow:** asks the user to select ink color rather than read the word. Color perception and familiarity with the task can affect performance; labels are available so meaning is not communicated by color alone.
- **Gaze Quest:** current build uses click-based target selection. It does not calculate gaze. Face landmarks alone would not constitute validated gaze tracking; calibration and uncertainty handling would be required.
- **Motion Sync:** current scoring uses mouse clicks. Camera preview does not drive collisions. A future hand-tracking implementation must only score a collision when a valid hand landmark is detected.

A single short session cannot measure intelligence, overall alertness, fatigue, ADHD, emotions or health. Scores should be interpreted only as results from that particular round.
