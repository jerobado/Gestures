## Contributing
First of all, thank you for considering to contribute in this volunteer project. If you're ready, let's get started.

1. [Requirements](#requirements)
2. [Setup virtual environment](#setup-virtual-environment)
3. [Running Gestures](#running-gestures)
4. [Development Workflow](#development-workflow)
5. [Submitting Pull Request](#submitting-pull-requests)
6. [Reminders](#reminders)

## Requirements
Here are the list of software tools and third party libraries that you need to have and install before you start developing:

* [Python]()
* [PyQt]() - for the Graphical User Interface (GUI)
* [keyboard](https://github.com/boppreh/keyboard) - a Python third party library responsible for _Gestures_ core operations

## Setup virtual environment

These steps will create a virtual environment and install the dependencies using `pipenv`:

1. Create virtual environment with specific python version

    ```
    pipenv --python 3.14
    ```

2. Activate the virtual environment

    ```
    pipenv shell
    ```

3. Install dependencies in your virtual environment

    ```
    pipenv update
    ```

4. Check installed version

    ```bash
    pipenv graph
    
    # output
    altgraph==0.17.4
    keyboard==0.13.5
    pefile==2023.2.7
    pyinstaller-hooks-contrib==2025.4
    ├── setuptools [required: >=42.0.0, installed: 80.4.0]
    └── packaging [required: >=22.0, installed: 25.0]
    PyQt6==6.9.0
    ├── PyQt6_sip [required: >=13.8,<14, installed: 13.10.0]
    └── PyQt6-Qt6 [required: >=6.9.0,<6.10.0, installed: 6.9.0]
    pywin32-ctypes==0.2.3
    ```

## Running Gestures

After setting up your virtual environment, you can now run the app by executing this command:

```
python -m src.main
```

This should display Gesture's main window.

## Development Workflow
Each private or open source project has its own development workflow which is tailored in their organization. So here are the steps that you need to consider while working on this project.

1. Fork _Gestures_
2. Switch to the `develop` branch
3. Make your own branch or commit directly to the `develop` branch
4. Submit Pull Requests

## Submitting Pull Requests
If this is your first time submitting a pull requests, you are not alone --we've been there. Just read [this guide](http://google.com) and you are good to go.

Once approved and merged, you can check your [first PR](http://firstpr.me) to celebrate your open source contribution. #hurray #firstPR

## Reminders
**Do commit in the `develop` branch**. All development commits are all happening in this branch and it is identifiable as `develop-[version_number]`.

**Do not commit on the `master` branch.** This branch is only use to deploy _Gestures_. The `develop` branch is only allowed to apply changes in this branch.
