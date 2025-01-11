# Python - Minimal Template Guide

This guide introduces a basic template for Python projects, designed to help you get started quickly and efficiently. It includes a straightforward project structure, pre-configured logging, and task management tools. Essential libraries are already included, so you can focus on your project without worrying about initial setup.

👉 You can explore additional templates through our tools or on our [Portal](https://robocorp.com/portal/tag/template).

---

## Overview
This template uses the [Python framework](https://github.com/robocorp/robocorp) and related [libraries](https://github.com/robocorp/robocorp/blob/master/docs/README.md#python-libraries) to provide a reliable foundation for your project.

### Architectural Model
![Diagram](https://github.com/user-attachments/assets/ec14a54c-ef61-4727-9ea6-04136cd1884c)

---

## How to Run the Project

### Using VS Code
1. Install the [Robocorp Code extension](https://robocorp.com/docs/developer-tools/visual-studio-code/extension-features).
2. Use the side panel and command palette for running, debugging, and accessing code completion and documentation.

### Using the Command Line
1. Download [RCC](https://github.com/robocorp/rcc?tab=readme-ov-file#getting-started).
2. Run the command: `rcc run`.

---

## Results

🚀 After running, check the `log.html` file located in the `output` folder.

---

## Managing Dependencies

We recommend adding your project dependencies to the [conda.yaml](conda.yaml) file. This helps manage the Python environment and ensures consistency across different machines.

<details>
  <summary>Why use conda.yaml?</summary>

Think of `conda.yaml` as an improved version of `requirements.txt`. It manages not only your Python packages but also the entire Python environment. Here’s why it’s better:

- Ensures your project runs seamlessly on other machines.
- Avoids issues with Python installations across devices.
- Lets you specify the exact Python and pip versions, preventing dependency conflicts.
- Removes the need for additional tools like `venv` or `pyenv`.
- Provides access to [conda-forge](https://prefix.dev/channels/conda-forge), simplifying dependency management.

> Learn more with [these resources](https://github.com/robocorp/rcc/blob/master/docs/recipes.md#what-is-in-condayaml).

</details>

---

## Additional Tools and Resources

- Full support for [rpaframework](https://robocorp.com/docs/python/rpa-framework) is included while the new Python libraries are being implemented.
- Start writing Python confidently—AI tools like Robocorp ReMark 💬 are available to assist you: [Try it here](https://chat.robocorp.com).

For more information:
- Visit the [Robocorp Documentation](https://robocorp.com/docs).
- Browse more examples on the [Portal](https://robocorp.com/portal).
- Follow our main [Robocorp repository](https://github.com/robocorp/robocorp) for updates and development progress.

---

🚀 Happy Coding! Start your project today and explore the possibilities.
