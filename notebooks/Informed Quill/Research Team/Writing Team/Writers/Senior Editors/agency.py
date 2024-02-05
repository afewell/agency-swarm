from agency_swarm import Agency

chief_editor = ChiefEditor()
editors = Editors()

agency = Agency([chief_editor, [chief_editor, editors]],
                shared_instructions='./agency_manifesto.md')

if __name__ == '__main__':
    agency.demo_gradio()