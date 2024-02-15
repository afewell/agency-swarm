from agency_swarm.agents import Agent


class AnalyzeInquiry(Agent):
    def __init__(self):
        super().__init__(
            name="AnalyzeInquiry",
            description="Analyzes incoming inquiries, categorizes them based on topic, identifies the technical depth required, and assesses the urgency. This helps in routing the inquiry to the appropriate response team.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools"
        )
