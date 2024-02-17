# eBurger GitHub Action
The GitHub action to add [eburger](https://github.com/forefy/eburger) into your workflow.

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
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          submodules: 'true' # change to 'recursive' if needed
      
      - name: Run eburger
        id: eburger
        uses: forefy/eburger-action@main # @main is recommended, although for improved stability change to the latest marketplace release (e.g. v1.0.1)
  
      - name: Upload SARIF file
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: ${{ steps.eburger.outputs.sarif }}
```

## Inputs

| Input                 | Description                                                             | Required | Default | 
|-----------------------|-------------------------------------------------------------------------|----------|---------|
| `path`                | Path of the folder or file to scan (relative to project root)           | `false`  | `.`     |
| `exclude`             | Exclude finding severities. e.g. "medium" will turn off medium and low  | `false`  |         |
| `automatic_selection` | If there are multiple projects in the repo, choose the N'th option      | `false`  | `1`     |
| `output_type`         | Results output file type                                                | `false`  | `sarif` |

## Outputs

| Output           | Description                                                               |
|------------------|---------------------------------------------------------------------------|
| `sarif`          | SARIF output (recommended)                                                |
| `json`           | JSON output                                                               |