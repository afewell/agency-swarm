from agency_swarm import Agency


agency = Agency([writing_director, [writing_director, writers],
 [writing_director, senior_editors]],
shared_instructions='./agency_manifesto.md')

if __name__ == '__main__':
    agency.demo_gradio()
