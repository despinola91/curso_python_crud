import click
from clients.services import ClientService
from clients.models import Client
from tabulate import tabulate

@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.option('-n', '--name',
                type=str,
                prompt=True,
                help='The client name')
@click.option('-c', '--company',
                type=str,
                prompt=True,
                help='The client company')
@click.option('-e', '--email',
                type=str,
                prompt=True,
                help='The client email')
@click.option('-p', '--position',
                type=str,
                prompt=True,
                help='The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new client"""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """Lists all clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()
    
    headers = [field.capitalize() for field in Client.schema()]
    table = []

    for client in client_list:
        table.append(
            [client['name'],
            client['company'],
            client['email'],
            client['position'],
            client['uid']
            ]
        )
    click.echo(tabulate(table, headers))


@clients.command()
@click.pass_context
def update(ctx, uid):
    """Updates a client"""
    pass

@clients.command()
@click.pass_context
def delete(ctx, uid):
    """Deletes a client"""
    pass


all = clients
