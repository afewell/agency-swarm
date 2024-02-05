from agency_swarm import Agency


agency = Agency([ceo, [ceo, research_team],
 [ceo, writing_team],
 [writing_team, writers],
 [writing_team, senior_editors]],
shared_instructions='./agency_manifesto.md')

if __name__ == '__main__':
    agency.demo_gradio()
