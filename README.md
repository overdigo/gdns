# gdns 📊

> A simple CLI tool to ping DNS servers and plot their query times directly in your terminal. Inspired by [gping](https://github.com/orf/gping).

This tool lets you quickly compare the performance of multiple DNS servers in a visual and easy-to-understand way, without leaving your command line.

## Demo

![gdns Demo](https://i.imgur.com/8n7gZkU.gif) 

*(This is a sample GIF, you can replace it with a real recording of gdns in action!)*

## Features

-   **Real-time Plotting**: Visualizes DNS query times in a live graph in your terminal.
-   **Multiple Servers**: Compare any number of DNS servers simultaneously.
-   **Customizable**: Test resolution against a specific domain using the `--domain` flag.
-   **Lightweight**: Built with Python, `dnspython`, and the awesome `plotext` for terminal graphing.

## Installation

To get started, clone the repository and set up the Python virtual environment.

```bash
# 1. Clone the repository (replace with your username)
git clone https://github.com/your-username/gdns.git

# 2. Navigate to the project directory
cd gdns

# 3. Create and activate a Python virtual environment
python3 -m venv venv
source venv/bin/activate

# 4. Install the required dependencies
pip install -r requirements.txt
```

## Usage

To run the tool, call the script with the Python interpreter from the virtual environment, followed by the IP addresses of the DNS servers you want to test.

**Basic Example:**

```bash
./venv/bin/python gdns.py 8.8.8.8 1.1.1.1
```

**Testing a specific domain:**

By default, `gdns` queries `google.com`. You can specify a different domain:

```bash
./venv/bin/python gdns.py 8.8.8.8 1.1.1.1 --domain wikipedia.org
```

**Pro-Tip: Create an Alias**

For easier access, you can add an alias to your shell's configuration file (`~/.bashrc`, `~/.zshrc`, etc.).

```bash
alias gdns='/path/to/your/gdns/venv/bin/python /path/to/your/gdns/gdns.py'
```

After adding the alias and reloading your shell, you can simply run:
`gdns 8.8.8.8 1.1.1.1`

## License

This project is licensed under the MIT License.
