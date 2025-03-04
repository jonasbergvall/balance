import streamlit as st
from streamlit_image_select import image_select

# Logo display
logo = '''
<div style="text-align: right; margin-bottom: 20px;">
    <img src="https://bestofworlds.se/img/BoWlogo.png" width="150px">
</div>
'''
st.markdown(logo, unsafe_allow_html=True)

def main():
    # Initialize session state variables with default values
    if 'page' not in st.session_state:
        st.session_state.page = 'start'
    if 'selections' not in st.session_state:
        st.session_state.selections = {
            'passion': 'balanced',    
            'authority': 'balanced',
            'action': 'balanced',
            'creation': 'balanced'
        }
    
    # Navigation logic
    if st.session_state.page == 'start':
        start_page()
    elif st.session_state.page == 'passion':
        passion_page()
    elif st.session_state.page == 'authority':
        authority_page()
    elif st.session_state.page == 'action':
        action_page()
    elif st.session_state.page == 'creation':
        creation_page()
    elif st.session_state.page == 'results':
        results_page()
    elif st.session_state.page == 'summary':
        summary_page()


def start_page():
    st.title("Welcome to the Organizational Balance Assessment")
    st.image("images/firstpage.webp",  use_container_width=True)
    st.markdown("""
    ### Discover the balance within your organization!
    
    This tool helps you visualize and understand the dynamics of your organization's culture across four key qualities:
    
    - **Passion**
    - **Authority**
    - **Action**
    - **Creation**
    
    You'll select images that best represent each quality in your organization. Let's get started!

    Contact us at [team@bestofworlds.se](mailto:team@bestofworlds.se) if you have any questions.
    """)
    if st.button("Start Assessment"):
        st.session_state.page = 'passion'
        st.rerun()

def passion_page():
    st.title("Passion")
    st.markdown("### Select the image that best represents Passion in your organization:")
    
    images = [
        "images/passion_deficient.webp",
        "images/passion_balanced.webp",
        "images/passion_excess.webp"
    ]
    captions = ["Lacking Passion", "Balanced Passion", "Too much Passion"]
    
    choice = image_select(
        label="",
        images=images,
        captions=captions,
        use_container_width=True
    )
    
    state = choice.split('_')[-1].replace('.webp', '').lower()
    st.session_state.selections['passion'] = state
    
    if st.button("Next"):
        st.session_state.page = 'authority'
        st.rerun()


def authority_page():
    st.title("Authority")
    st.markdown("### Select the image that best represents Authority in your organization:")
    
    images = [
        "images/authority_deficient.webp",
        "images/authority_balanced.webp",
        "images/authority_excess.webp"
    ]
    captions = ["Unclear Authority", "Balanced Authority", "Egocentric Authority"]
    
    choice = image_select(
        label="",
        images=images,
        captions=captions,
        use_container_width=True
    )
    
    state = choice.split('_')[-1].replace('.webp', '').lower()
    st.session_state.selections['authority'] = state

    
    if st.button("Next"):
        st.session_state.page = 'action'
        st.rerun()

def action_page():
    st.title("Action")
    st.markdown("### Select the image that best represents Action in your organization:")
    
    images = [
        "images/action_deficient.webp",
        "images/action_balanced.webp",
        "images/action_excess.webp"
    ]
    captions = ["Not enough Action", "Balanced Action", "Too much Action"]
    
    choice = image_select(
        label="",
        images=images,
        captions=captions,
        use_container_width=True
    )
    
    state = choice.split('_')[-1].replace('.webp', '').lower()
    st.session_state.selections['action'] = state
    
    if st.button("Next"):
        st.session_state.page = 'creation'
        st.rerun()

def creation_page():
    st.title("Creation")
    st.markdown("### Select the image that best represents Creation in your organization:")
    
    images = [
        "images/creation_deficient.webp",
        "images/creation_balanced.webp",
        "images/creation_excess.webp"
    ]
    captions = ["Unfocused Creation", "Balanced Creation", "Manipulative Creation"]
    
    choice = image_select(
        label="",
        images=images,
        captions=captions,
        use_container_width=True
    )
    
    state = choice.split('_')[-1].replace('.webp', '').lower()
    st.session_state.selections['creation'] = state
    
    if st.button("View Organizational Profile"):
        st.session_state.page = 'results'
        st.rerun()

def results_page():
    st.title("Your Organizational Profile")
    
    selections = {
        'passion': st.session_state.selections.get('passion', 'balanced'),
        'authority': st.session_state.selections.get('authority', 'balanced'),
        'action': st.session_state.selections.get('action', 'balanced'),
        'creation': st.session_state.selections.get('creation', 'balanced')
    }
    
    narrative = generate_narrative(selections)
    strategies = suggest_strategies(selections)
    roles = suggest_roles(selections)
    
    st.markdown("### Results")
    st.write(narrative)
    
    st.markdown("### Suggested Strategies")
    st.write(strategies)
    
    st.markdown("### New Roles")
    st.write(roles)
    
    if st.button("Next Step"):
        st.session_state.page = 'summary'
        st.rerun()
    
    if st.button("Restart Assessment"):
        st.session_state.page = 'start'
        st.session_state.selections = {}
        st.rerun()

# New function for a personalized consultant-style summary
def summary_page():
    st.title("Consultant's Summary")
    selections = st.session_state.selections
    summary = generate_consultant_summary(selections)
    st.write(summary)
    
    # Add navigation buttons
    if st.button("Back to Results"):
        st.session_state.page = 'results'
        st.rerun()
    
    if st.button("Restart Assessment"):
        st.session_state.page = 'start'
        st.session_state.selections = {}
        st.rerun()


def generate_consultant_summary(selections):
    # Get narrative, strategies, and roles in paragraph form
    narratives = generate_narrative(selections, as_bullets=False)
    strategies = suggest_strategies(selections, as_bullets=False)
    roles = suggest_roles(selections, as_bullets=False)
    
    # Combine into a flowing consultant-style text
    summary = (
        "Based on your selections, here is a comprehensive overview of your organization’s culture, "
        "drawing upon foundational qualities of Passion, Authority, Action, and Creation. Together, these energies form the backbone "
        "of a cohesive, resilient organizational environment.\n\n"
        f"{narratives}\n\n"
        "To foster greater balance and alignment, consider the following strategies that encourage each quality to work harmoniously with the others:\n\n"
        f"{strategies}\n\n"
        "Additionally, certain roles can serve as guardians of these energies, ensuring that each quality is expressed fully and harmoniously:\n\n"
        f"{roles}\n\n"
        "By implementing these strategies and roles, your organization can address imbalances, cultivate resilience, and build a "
        "supportive environment where each team member is motivated to contribute meaningfully. This process of aligning core energies "
        "brings an integrated, holistic approach to your organization’s growth and adaptability."
    )
    
    return summary

def generate_narrative(selections, as_bullets=True):
    narratives = {
        'passion': {
            'balanced': "Your organization embodies a harmonious expression of Passion. Team members are motivated by shared purpose and collective enthusiasm, contributing vitality and warmth to the environment.",
            'excess': "Passion flows intensely within your organization, but there is a risk of it tipping into burnout if not channeled with focus and intention.",
            'deficient': "Passion feels muted, and the organizational atmosphere may lack the spark that fosters engagement and morale, which could impact team cohesion."
        },
        'authority': {
            'balanced': "Authority is exercised as a guiding presence, fostering stability, trust, and inclusivity. This balanced Authority supports Action by providing clear direction and aligns with Creation by nurturing a safe space for innovation.",
            'excess': "Authority is strong but may be overly concentrated, creating an environment that feels controlled rather than guided, which can inhibit collaboration.",
            'deficient': "There may be a lack of clear Authority, leading to uncertainty and a lack of unity in decision-making, which can cause challenges in coordinating actions and ideas."
        },
        'action': {
            'balanced': "Action within the organization is purposeful and aligned with the broader mission. Ambition is balanced with mindfulness, ensuring that productivity is sustainable and values-driven.",
            'excess': "Action flows relentlessly, driven by urgency, which can lead to exhaustion and hinder reflective practices that would support long-term success.",
            'deficient': "Action is hesitant or overly cautious, relying on routine rather than innovation, which could prevent the organization from advancing effectively."
        },
        'creation': {
            'balanced': "Creativity is nurtured in a balanced way, encouraging innovation while aligning with the organization’s goals. Team members feel inspired to explore new ideas within a structured framework.",
            'excess': "Creativity abounds, yet without shared focus, ideas may remain unanchored, leading to inefficiencies and scattered priorities.",
            'deficient': "Creativity feels constrained, limited by tradition or lack of support for novel approaches, which can stifle growth and adaptability."
        }
    }
    
    narrative_text = " ".join([narratives[quality][selections[quality]] for quality in selections])
    return narrative_text if not as_bullets else "\n".join([f"- {narratives[quality][selections[quality]]}" for quality in selections])

def suggest_strategies(selections, as_bullets=True):
    strategies = {
        'passion': {
            'excess': "Channel Passion toward collective goals, ensuring enthusiasm remains sustainable over time.",
            'deficient': "Create spaces for open dialogues and shared purpose to reignite Passion and engagement.",
            'balanced': "Continue practices that support balanced Passion, maintaining the organization’s vitality and collective drive."
        },
        'authority': {
            'excess': "Encourage participatory frameworks to create a balance in Authority, fostering collaborative decision-making.",
            'deficient': "Establish clear leadership roles to reinforce structure and direction, providing a foundation of confidence.",
            'balanced': "Maintaining balanced Authority reinforces trust and stability within the organization."
        },
        'action': {
            'excess': "Integrate reflective practices to sustain productivity and ensure actions align with long-term objectives.",
            'deficient': "Empower team members to take initiative, clarifying goals to enhance responsiveness.",
            'balanced': "Continue balancing productivity and mindfulness, supporting sustainable focus and adaptability."
        },
        'creation': {
            'excess': "Focus creative energy towards shared goals to align ideas with practical outcomes.",
            'deficient': "Encourage creativity by fostering a culture of innovation, making space for exploration and growth.",
            'balanced': "Balanced Creation supports adaptability and innovation—maintain practices that foster this balance."
        }
    }
    
    strategies_text = " ".join([strategies[quality][selections[quality]] for quality in selections])
    return strategies_text if not as_bullets else "\n".join([f"- {strategies[quality][selections[quality]]}" for quality in selections])

def suggest_roles(selections, as_bullets=True):
    roles = {
        'passion': {
            'balanced': "An **Inspiration Catalyst** could enhance this balanced Passion, fostering a culture of purpose and collective enthusiasm.",
            'excess': "A **Purpose Architect** might help channel Passion sustainably, aligning energy with long-term goals.",
            'deficient': "An **Engagement Energizer** could be vital in reigniting morale, helping reconnect individuals to the organization’s mission."
        },
        'authority': {
            'balanced': "A **Trust Steward** ensures Authority remains balanced, supporting a transparent and inclusive environment.",
            'excess': "A **Boundary Harmonizer** may bring balance to Authority, encouraging shared decision-making.",
            'deficient': "A **Direction Guide** would provide structure and confidence, reinforcing leadership clarity."
        },
        'action': {
            'balanced': "An **Outcome Navigator** supports balanced Action, ensuring efforts contribute to the organization’s broader purpose.",
            'excess': "A **Pace Designer** could introduce sustainable productivity practices, preventing burnout.",
            'deficient': "An **Activation Enabler** could empower team members, fostering initiative and drive."
        },
        'creation': {
            'balanced': "An **Innovation Weaver** nurtures balanced Creation, blending fresh ideas with practicality.",
            'excess': "A **Vision Curator** provides structure, prioritizing ideas and aligning resources effectively.",
            'deficient': "A **Creative Catalyst** could encourage creative problem-solving, fostering an innovative atmosphere."
        }
    }
    
    roles_text = " ".join([roles[quality][selections[quality]] for quality in selections])
    return roles_text if not as_bullets else "\n".join([f"- {roles[quality][selections[quality]]}" for quality in selections])


    

if __name__ == '__main__':
    main()
