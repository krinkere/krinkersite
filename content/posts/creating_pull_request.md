Title: How to create pull request for github
Date: 2018-08-24 15:40
Modified: 2018-08-24 15:55
Status: published
Category: Coding
Tags: git, coding
Slug: How_to_create_pull_request_for_github
Authors: Al Krinker
Summary: Steps that you need to take in order to submit pull request to an open source project

The Steps:<br />
1. Fork a a project that you are trying to fix to your own github and clone it <br />
2. Create new branch: git checkout -b fix-test-validation <br />
3. git add --what you modified-- <br />
4. git commit <br />
5. git log (to see your changes) <br />
6. git branch (to verify where you are) <br />
7. git push origin fix-test-validation (to push it to the git) <br />
8. Go to github and click on "Compare & pull request" <br />
9. Add comment and click 'Create pull request' when done. <br />
10. At that point, your work is done and someone with permissions would validate the request and do a pull. <br />