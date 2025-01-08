import settings
import image_settings

def convertToLinkedinPrompt(
    transcript,
    number_of_posts=settings.number_of_posts,
    tone=settings.tone,
    style=settings.style,
    length=settings.length,
    hook_type=settings.hook_type,
    cta_type=settings.cta_type,
    emoji_preference=settings.emoji_preference,
    spacing=settings.spacing,
    formatting=settings.formatting,
    hashtag_preference=settings.hashtag_preference,
    industry=settings.industry,
    target_audience=settings.target_audience,
    brand_voice=settings.brand_voice,
    creator_style=settings.creator_style,
    focus=settings.focus,
    experience=settings.experience,
    perspective=settings.perspective,
    cultural_context=settings.cultural_context,
    angle=settings.angle
):
    """Converts a transcript to a LinkedIn prompt"""
    prompt = """
        You are a professional content creator specializing in LinkedIn posts. Create {number_of_posts} LinkedIn post(s) based on the following inputs and parameters:
        SOURCE CONTENT:

        YouTube Video Transcript: {transcript}

        STYLE PARAMETERS:

        Tone: {tone} [Options: Professional, Casual, Gen-Z, Motivational, Educational, Technical]
        Writing Style: {style} [Options: Story-based, Data-driven, Question-based, List format, Problem-solution]
        Post Length: {length} [Options: Short (< 800 chars), Medium (800-1500 chars), Long (1500-3000 chars)]
        Hook Style: {hook_type} [Options: Question, Statistic, Bold Statement, Personal Story, Contrarian View]
        Call-to-Action Type: {cta_type} [Options: Soft CTA, Strong CTA, Question-based CTA, None]

        FORMATTING PREFERENCES:

        Emoji Usage: {emoji_preference} [Options: None, Minimal (1-2), Moderate (3-5), Heavy (6+)]
        Line Spacing: {spacing} [Options: Compact, Regular, Airy]
        Text Formatting: {formatting} [Options: Plain, With Bold Points, With Bullet Points]
        Hashtag Usage: {hashtag_preference} [Options: None, Minimal (1-3), Moderate (4-6), Heavy (7+)]

        BRANDING ELEMENTS:

        Industry: {industry}
        Target Audience: {target_audience}
        Brand Voice: {brand_voice} [Options: Authoritative, Friendly, Innovative, Traditional]
        Creator Inspiration: {creator_style}
        Key Message Focus: {focus} [Options: Educational, Inspirational, Problem-solving, Thought Leadership]

        PERSONALIZATION:

        Personal Experience Level: {experience} [Options: Beginner, Intermediate, Expert]
        Unique Perspective: {perspective} [Options: First-hand experience, Research-based, Opinion, Case study]
        Cultural Context: {cultural_context} [Options: Global, Region-specific, Industry-specific]
        Content Angle: {angle} [Options: Success story, Learning experience, Industry insight, Trend analysis]

        Create {number_of_posts} unique LinkedIn posts that are:

        Engaging and scroll-stopping
        Relevant to the source content
        Formatted according to the specified preferences
        Aligned with the chosen creator's style while maintaining authenticity
        Optimized for LinkedIn's algorithm

        Format each post as:
        Post 1:
        [Post content]
        Post 2:
        [Post content]
        Post 3:
        [Post content]
    """.format(
        transcript=transcript,
        tone=tone,
        style=style,
        length=length,
        hook_type=hook_type,
        cta_type=cta_type,
        emoji_preference=emoji_preference,
        spacing=spacing,
        formatting=formatting,
        hashtag_preference=hashtag_preference,
        industry=industry,
        target_audience=target_audience,
        brand_voice=brand_voice,
        creator_style=creator_style,
        focus=focus,
        experience=experience,
        perspective=perspective,
        cultural_context=cultural_context,
        angle=angle,
        number_of_posts=number_of_posts
    )

    return prompt

def convertResponseToImage(
    response,
    diagram_type=image_settings.diagram_type,
    color_scheme=image_settings.color_scheme,
    font_style=image_settings.font_style,
    icon_preference=image_settings.icon_preference,
    layout_orientation=image_settings.layout_orientation,
    target_audience=image_settings.target_audience
):

    iprompt =  """
       You are a professional content creator specializing in visual storytelling. Based on the following AI-generated LinkedIn post(s), 
       create a diagram in SVG format that visually represents the key concepts, relationships, and ideas from the post(s),
       in your output always just provide the code for the svg file, nothing else. 

        **INPUT DETAILS:**

        LinkedIn Post Content:
        {response}

        **STYLE PARAMETERS:**

        1. **Diagram Type**: {diagram_type} [Options: Flowchart, Mind Map, Hierarchical Diagram, Venn Diagram, Process Diagram]
        2. **Color Scheme**: {color_scheme} [Options: Minimalist (Black & White), Vibrant (Bright Colors), Brand Colors (Industry-specific)]
        3. **Font Style**: {font_style} [Options: Serif, Sans-serif, Handwritten]
        4. **Iconography**: {icon_preference} [Options: None, Minimal, Detailed]
        5. **Layout Orientation**: {layout_orientation} [Options: Horizontal, Vertical, Radial, Freeform]
        6. **Target Audience**: {target_audience} [Options: General Audience, Students, Teachers, Children]

        **CONTENT REPRESENTATION:**

        - Each key idea or paragraph from the LinkedIn post should be represented as a node or section in the diagram.
        - Relationships between ideas should be depicted using arrows, lines, or connectors.
        - Summarize and simplify where necessary to ensure clarity and focus.
        - A title that captures the overall topic, at the top of the diagram.

        **FORMATTING REQUIREMENTS:**

        - Output must be an SVG file that can scale seamlessly.
        - Output must be 1080 x 1080 pixels.
        - In the .svg file, replace the '&' character with its valid XML entity code, '&amp;'
        - Use descriptive IDs and classes for all SVG elements for easy customization.
        - Ensure readability and accessibility by adhering to design best practices (e.g., proper contrast, legible fonts).
        - Cross check each coordinate to make sure nothing is overlapping, the lines and circles aren't disconnected 
          (unless if its the style), all text is clear and visible and the font size isn't small (this post is going to be viewed on a 
          phone with a 1080 x 1080 image window).
        - Maintain symmetry between the distance of the objects that is visually appealing.

        **OUTPUT EXAMPLE FORMAT:**

        ```svg
        <svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
        <!-- Example Node -->
        <rect x="50" y="50" width="200" height="50" fill="#FFA500" />
        <text x="150" y="75" font-family="Sans-serif" font-size="14" text-anchor="middle" fill="#FFFFFF">Key Idea</text>
        <!-- Example Arrow -->
        <line x1="150" y1="100" x2="150" y2="150" stroke="#000000" stroke-width="2" />
        </svg> 

    """.format(
        response=response,
        diagram_type=diagram_type,
        color_scheme=color_scheme,
        font_style=font_style,
        icon_preference=icon_preference,
        layout_orientation=layout_orientation,
        target_audience=target_audience
    )
    
    return iprompt