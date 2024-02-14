# eBurger GitHub Action
The GitHub action to add [eBurger](https://github.com/forefy/eburger) into your workflow.

For more information check the main repository: https://github.com/forefy/eburger.

## Usage
```yaml
name: eBurger Static Analysis
on: [push]
jobs:
  analyze:
    runs-on: ubuntu-latest
    permissions:
      security-events: write
      # only required for workflows in private repositories
      # actions: read
      # contents: read
      
    steps:
      - uses: actions/checkout@v4
      - run: git submodule init
      - run: git submodule update
      
      - name: Run eBurger
        uses: forefy/eburger-action@main
        id: eburger
  
      - name: Upload SARIF file
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: ${{ steps.eburger.outputs.sarif }}
```

## Inputs

| Input            | Description                                                               | Required | Default | 
|------------------|---------------------------------------------------------------------------|----------|---------|
| `path`           | Path of the folder or file to scan (relative to project root)             | `false`  | `.`     |
| `exclude`        | Exclude finding severities. e.g. "medium" will turn off medium and low.   | `false`  |         |
| `output_type`    | Results output file type.                                                 | `false`  | `sarif` |

## Outputs

| Output           | Description                                                               |
|------------------|---------------------------------------------------------------------------|
| `sarif`          | SARIF output                                                              |
| `json`           | JSON output                                                               |