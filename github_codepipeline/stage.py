import aws_cdk as cdk
from constructs import Construct
from github_codepipeline.storage import Storage



class Stage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        

        bucket = Storage(
            self, 
            "Storage"                  
        )
