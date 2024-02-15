from agency_swarm.agents import Agent


class ARAChief(Agent):
    def __init__(self):
        super().__init__(
            name="ARAChief",
            description="Acts as the entry point for communication, overseeing the operations and ensuring that processes run smoothly and efficiently.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools"
        )
