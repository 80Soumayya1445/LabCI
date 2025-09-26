# Advanced CI Exercise: Multi-Stage Workflow with Caching and Matrix Builds

## Objective

In this exercise, you will build a **multi-stage Continuous Integration (CI) workflow** that:
- Uses **matrix builds** to test across multiple environments
- Implements **dependency caching** for faster runs
- Runs separate **lint, test, and build stages**
- Uploads build artifacts


## Prerequisites
- GitHub repository with a project (Node.js or Python)
- If you choose a javascript project you can use the following for https://medium.com/@robert_mcbryde/linters-for-beginners-4ff01c6279dc as it includes steps for lining

## Instructions

### Step 1: Create the Workflow File
1. In your repository, create a workflow file named `ci.yml`

### Step 2: Define the Workflow
Your workflow should:
1. Trigger on:
- Pushes to the `main` branch
- Pull requests to `main`
2. Use a [**matrix strategy**](https://www.geeksforgeeks.org/git/the-matrix-strategy-in-github-actions/) to run jobs on:
- Node.js versions `16` and `18`
- Operating systems: `ubuntu-latest` and `windows-latest`
3. Include **job caching** for dependencies:
- Cache `node_modules` (for Node.js projects) or `.venv` (for Python)
4. Have **multiple stages**:
- **Lint stage**: Run `npm run lint` (or equivalent for your project)
- **Test stage**: Run your test suite
- **Build stage**: Run `npm run build` (or equivalent) and upload build artifacts


#### Linter Setup (for JavaScript projects)

If your project does not already have a linter, follow these steps to set up **ESLint**:

### Step 3: Push and Verify
1. Commit and push the workflow to your repo.
2. Open the **Actions tab** on GitHub.
3. Verify:
- Each job runs in multiple environments (matrix)
- Dependency caching is applied
- Lint, test, and build all run in sequence
- Build artifacts are uploaded and can be downloaded from the run (for building you can just copy the main file in a dist folder)

### Step 4: Experiment
- Break your linting rules or tests to see CI fail
- Fix the issues and push again
- Observe the green checkmark when everything passes

### Step 4: Enhancement
- Add a **code coverage report** and upload it as an artifact
- Configure your workflow to only build if tests pass



