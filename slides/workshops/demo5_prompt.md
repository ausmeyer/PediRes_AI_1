# Demonstration 5 prompt

Open `broken_attendance.html` in a browser and reproduce the interaction issue. Then inspect and repair the existing file; do not replace it with a framework or add dependencies.

Acceptance tests:

1. The page loads without a console error.
2. The week labels remain 1 through 8 and the attendance counts remain exactly `19, 22, 17, 25, 23, 20, 26, 24`.
3. Entering a whole number from 1 through 8 highlights exactly the matching bar in orange and reports the matching count.
4. Entering anything else highlights no bar and displays the exact message `Enter a week from 1 to 8.`
5. The file makes no external API, library, font, or network request.
6. The input has an accessible label and the status message is announced to assistive technology.

After editing, test inputs `4`, `1`, `8`, `9`, and a blank value. Report the cause of the issue, the specific edit, and the test results.
