from agency_swarm.agents import Agent


class CraftResponse(Agent):
    def __init__(self):
        super().__init__(
            name="CraftResponse",
            description="Focuses on formulating detailed and accurate responses to inquiries. Ensures the responses reflect the technical depth and professional tone suitable for the audience from prestigious analytical firms.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools"
        )
