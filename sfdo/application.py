import click
import shutil
from pathlib import Path
from jinja2 import Environment, PackageLoader
from datetime import date

BLOGDIR = Path("/Users/jeff/Code/strykeforce/strykeforce.org/content/blog")


class Application:
    def __init__(self):
        self.date = date.today()
        self.year = f"{self.date.year}"
        self.month = f"{self.date.month:02}"
        self.day = f"{self.date.day:02}"

    def prompt(self):
        self.title = click.prompt("Title")
        self.blurb = click.prompt("Blurb")
        self.description = click.prompt("Description", self.blurb)
        self.author = click.prompt("Author")
        self.draft = click.prompt("Draft", False, type=click.BOOL)
        self.slug = click.prompt("Slug")
        self.body = click.prompt("Body")
        self.cover: Path = click.prompt(
            "Cover", "/Users/jeff/Desktop/cover.jpg", type=Path
        )

        self.base = f"blog/{self.year}/{self.month}/{self.day}-{self.slug}"

    def render(self):
        env = Environment(loader=PackageLoader("sfdo"), autoescape=False)
        dir = BLOGDIR / self.year / self.month / f"{self.day}-{self.slug}"
        dir.mkdir(parents=True, exist_ok=False)
        with open(dir / "index.md", "w") as f:
            f.write(env.get_template("blog.md.j2").render(self.__dict__))
        shutil.copy(self.cover, dir)


def main() -> None:
    app = Application()
    app.prompt()
    app.render()


if __name__ == "__main__":
    main()
