# Contributing

## New features

For any feature level changes, advance planning is required. Please raise a [feature request](https://github.com/ByAnthony/nztunnellers/issues/new?assignees=&labels=&projects=&template=feature_request.md&title=) to start a conversation with codeowners.

## Other contributions

### Bug fixes

Please raise a [bug report](https://github.com/ByAnthony/nztunnellers/issues/new?assignees=&labels=&projects=&template=bug_report.md&title=) to start a conversation with codeowners.

### Others

For non-feature work (service improvements, changes that contribute to existing defined patterns) you are more than welcome to contribute and hope to make your life easy when raising them.

The process is:

- Read the [docs](../docs/);
- git clone the repository and follow our [getting started guide](./getting-started.md);
- To run the web app locally follow instructions in the [running locally guide](./running-locally.md);
- Raise a pull request;
- Ask for codeowner reviews.

## Pull Request

It's not always easy, but small pull requests are a hell of a lot easier for the reviewer.

Always feel free to hash out a complete solution on a branch to get your head straight on how you'll implement your solution and use as a demo - but when you're making the solution for real, try to raise pull request in comfortably-reviewable stages.

Be sure to leave a description in your pull request saying how/what you've made fits into the complete solution.

### pre-commit

We are using **pre-commit** to ensure some various checks before you are able to raise a pull request. Github Actions is setup to run the same steps when the pull request is raised.
