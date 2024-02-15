from agency_swarm import Agency
from CraftResponse import CraftResponse
from AnalyzeInquiry import AnalyzeInquiry
from ARAChief import ARAChief

ara_chief = ARAChief()
analyze_inquiry = AnalyzeInquiry()
craft_response = CraftResponse()

agency = Agency([ara_chief, [ara_chief, analyze_inquiry],
                 [analyze_inquiry, craft_response]],
                shared_instructions='./agency_manifesto.md')

if __name__ == '__main__':
    agency.demo_gradio()