import click



@click.command()
@click.option('-b', '--base_salary', default=0, help='Your base salary')
def main(base_salary):
    pass


if __name__ == '__main__':
    main()
