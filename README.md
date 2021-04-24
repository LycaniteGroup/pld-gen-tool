# PLD Generation Tool

The PLD Generation Tool is tool that we made to help us generate good looking pdf
directly from github issue.

## Install

Before doing anything you have to install to install python3
then install the required dependencies by running **install.sh**

```shell
chmod +x ./install.sh
./install.sh
```

## PLD Generation

The PLD Generation is done in multiple steps:
- Conversion of github issues to Markdown
- Conversion of Markdown to HTML
- Conversion of HTML to PDF
  
### Convert github issues to Markdown

Simply run the file **mkgen.sh**
```shell
chmod +x ./mkgen.sh
./mkgen.sh
```

You will next be prompted with a message asking you to choose an Authentication method to login to your Github account.

Choose **Token** authentication.

Next you will be asked to select the sprint you want to convert to Markdown.
Once done the conversion will begin.
The converted version of the sprint can be found in folder `sprints/{{Sprint Name}}/index.md` and can be edited before converting it to PDF.
You can also add a file named `sprints/{{Sprint Name}}/bilan.md`, this fill will be used to add a bilan for the sprint.

### Convert from Markdown to PDF

Simply run the file **mkbuild.sh**
```shell
chmod +x ./mkbuild.sh
./mkbuild.sh
```

This will run the build pipeline and output the pdf in the `build` folder

#### version.json

This file is used to update the revision number of the PDF, dont forget to bump the version before building the PLD

```json
{
    "revision": 2
}
```