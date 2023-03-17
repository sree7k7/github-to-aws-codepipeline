import aws_cdk as core
import aws_cdk.assertions as assertions

from github_codepipe.github_codepipe_stack import GithubCodepipeStack

# example tests. To run these tests, uncomment this file along with the example
# resource in github_codepipe/github_codepipe_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = GithubCodepipeStack(app, "github-codepipe")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
