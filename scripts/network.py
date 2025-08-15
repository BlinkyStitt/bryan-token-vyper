import click
from ape.cli import ConnectedProviderCommand

@click.command(cls=ConnectedProviderCommand)
def cli(ecosystem, network, provider):
    click.echo(f"Connected to {ecosystem.name}:{network.name} using provider '{provider.name}'.")
    
    # Access chain and other managers automatically
    from ape import chain
    click.echo(f"Current block: {chain.blocks.height}")
