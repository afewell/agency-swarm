from agency_swarm import Agency


agency = Agency([ceo, [ceo, researcher],
 [ceo, writer],
 [ceo, editor],
 [researcher, writer]],
shared_instructions='./agency_manifesto.md')

if __name__ == '__main__':
    agency.demo_gradio()
