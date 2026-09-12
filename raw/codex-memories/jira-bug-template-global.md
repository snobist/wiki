# Jira Bug Template (Global)

Use this template for ANY bug ticket creation request in any chat.

## Usage rules
- Treat this as the default bug description structure.
- Do not assume project/team/component/internal values unless the user explicitly provides them.
- Discover required fields for the target project/issue type at creation time.
- If mandatory fields are missing, ask for only those missing mandatory values.

## Description template
*Description*
[Short description of a problem in narrative form]

*Pre-conditions*
bq.Optional. Please delete if not filled

*Steps to reproduce*
# [Step 1]
# [Step 2]
# [Step N]

*Actual Result*
[The most complete description of actual results]

*Expected Result*
[(!) Besides stating what the expected result is please provide the reasoning for this - requirement, previous production behavior, etc.]

*Regression from version (not reproducible on):* <version>
_[(!) if regression from the previous version confirmed, set *Regression* flag to *Yes* and (if exact build known) write build on which issue started to reproduce into the *Broken* field.]_

*Automation Test Failed:*
[Please delete if not filled. Provide failed automation test name if any]
