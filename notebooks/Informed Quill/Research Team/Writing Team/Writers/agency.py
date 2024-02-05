from agency_swarm import Agency


agency = Agency([lead_writer, [lead_writer, blog_writers]],
shared_instructions='./agency_manifesto.md')

if __name__ == '__main__':
    agency.demo_gradio()
