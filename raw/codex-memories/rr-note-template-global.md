# RR Note Template (Global)

Use this template when the user asks for an RR note.

## Usage rules
- Treat this as the default RR note structure.
- Preserve the `@RR@` note type marker exactly.
- Delete optional sections only when preparing a final note and the section is not filled.
- Keep mandatory guidance in place until the required information is provided.

## Note template
*Note type: @RR@*

*Description:*
[Optional. Please delete if not filled. Describe actual behavior vs expected behavior]

*Workaround:*
[Optional. Please delete if not filled. Describe possible workaround]

*Root Cause:*
[Meaningful explanation of the issue root cause]

*Change Description:*
[description of changes performed to fix the issue]

*Automated Testing:*
[Mandatory for customer bug fixes. Optional for Internal Bugs and Gaps. Description of how the code change is tested automatically.
Please provide links to Merge Requests (unit tests and/or functional tests) or separate Jira tickets.
Please provide justification if there are no tests available.
Remember that auto-test of bugs should cover both Feature ON and OFF states.]

*Testing Hints:*
[Optional for Bugs, mandatory for Gaps. Description or hints on how to test the code change]

*Side effects:*
[Optional. Please delete if not filled. The list of impacted system components]

*Definition of Done*
[Optional. Please delete if not filled. Please provide DoD for the task completed]
