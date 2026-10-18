# Python TCP Client–Server

A Python networking project exploring TCP socket communication, multithreading, client connections, and interactive connection management.

This project was created as a hands-on learning exercise to understand how a server listens for incoming connections, how clients connect over a network, and how Python can manage multiple client connections.

> **Security notice:** The current implementation includes remote command execution through `subprocess.Popen(..., shell=True)`. Running it can allow commands received over the network to execute on the client machine. Use only in an isolated lab with systems you own or have explicit permission to test. Do not expose it to public networks or use it on untrusted devices.

## Features

- **TCP socket communication** — Uses Python's built-in `socket` module.
- **Connection listener** — Binds to a port and listens for incoming client connections.
- **Multiple client connections** — Maintains lists of active connections and their addresses.
- **Threading** — Uses worker threads to separate connection handling from the interactive interface.
- **Interactive terminal interface** — Includes commands for listing connections and selecting a client.
- **Working-directory handling** — The client attempts to support directory changes through received commands.
- **Standard output and error handling** — Captures command output and sends it back over the socket.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| `socket` | TCP networking |
| `threading` | Concurrent execution |
| `queue` | Worker job management |
| `subprocess` | Process execution in the current implementation |
| `os` | Operating-system and directory operations |

No third-party Python packages are required by the code shown.

## Project Structure

```text
python-tcp-client-server/
├── server.py
├── client.py
└── README.md
```

## Requirements

- Python 3
- Two terminal sessions for local testing
- A private, isolated test environment
- Permission to test every device involved

Check your Python installation:

```bash
python3 --version
```

## Configuration

The server listens on TCP port `9999`.

In `server.py`, the host is configured as an empty string, which means the server binds to the available local IPv4 interfaces.

In `client.py`, replace the placeholder server address with the IP address of your authorized test server:

```python
host = "SERVER_IP_ADDRESS"
port = 9999
```

Keep testing within a controlled lab environment. The current implementation does not provide authentication, encrypted communication, or a secure authorization protocol.

## Running the Project

1. Start the server in the first terminal:

   ```bash
   python3 server.py
   ```

2. Start the client in a second terminal on an authorized test machine:

   ```bash
   python3 client.py
   ```

3. Observe the connection messages and server-side client list.

**Important:** The implementation has known limitations, including recursive socket-binding retries, incomplete exception handling, shared-list concurrency issues, and potentially blocking socket reads. It should not be considered production-ready.

## Learning Objectives

This project helped me explore:

- TCP connection establishment and socket lifecycle.
- The difference between a server and a client.
- IP addresses, ports, and network interfaces.
- Basic concurrency using Python threads.
- Managing connected clients and their network addresses.
- Debugging socket errors such as `ConnectionRefusedError` and `Address already in use`.
- Understanding the security implications of executing data received over a network.

## Limitations

- No authentication or encrypted transport.
- No robust message-framing protocol.
- No reliable reconnect mechanism.
- Incomplete handling of client disconnections.
- Potential deadlocks and recursion errors.
- Remote command execution makes the current design unsafe for untrusted networks.

## Future Improvements

- Replace arbitrary remote command execution with a safe message-based protocol.
- Introduce message framing and connection timeouts.
- Use thread-safe connection management.
- Add structured logging and graceful shutdown.
- Add unit tests for connection failures and dropped connections.
- Implement authentication and encrypted communication for any future authorized remote-management features.

## Disclaimer

This repository is intended for educational study of Python networking and concurrency. Any testing must be limited to systems you own or are explicitly authorized to test. The current implementation is experimental and is not intended for production deployment.

## License

Choose an appropriate open-source license before publishing this repository. For example, the MIT License is a common option for projects intended to be reused and modified.
