from agency_swarm import Agency


agency = Agency([research_director, [research_director, research_analysts]],
shared_instructions='./agency_manifesto.md')

if __name__ == '__main__':
    agency.demo_gradio()
