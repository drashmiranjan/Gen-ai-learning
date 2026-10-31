from langchain_text_splitters import CharacterTextSplitter
text = '''You don't want to build an agent only for yourself. You want to build a platform where anyone can connect their professional profile, describe their services, and have an AI agent find potential customers for them.

A software developer finds software projects. A designer finds design clients. A video editor finds creators who need editing. A marketing agency finds businesses that need marketing.

The user defines the goal; the agent finds the opportunities.

Eventually, it could become a local-first, multi-agent platform that performs much of the repetitive business development work automatically, while keeping the user in control of consequential actions.

And because you're unemployed and have no hosting or domain budget, we start by building and running it on your own computer using free tools wherever possible.

Tell me if this is the idea you mean: an AI agent that doesn't merely show leads, but actively works to find clients and help win business on behalf of its use
'''
spilter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)
res = spilter.split_text(text)

print(res[0])