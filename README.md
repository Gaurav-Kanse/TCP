# Python TCP Reverse-Shell Experiment

A small Python networking project created to study TCP sockets, client/server communication, and how data can be exchanged between two processes over a network.

> [!CAUTION]
> **This code executes commands received over a network.** The client uses `subprocess.Popen(..., shell=True)`, so input received from the server can run as operating-system commands on the client machine. The implementation has no authentication or encryption. Treat it as an educational code sample only: do not run it on devices you do not own or administer, do not use it without explicit authorization, and never expose it to the public internet or an untrusted network.

## Project Structure

```text
TCP/
├── README.md
└── Reverseshell/
    ├── server.py
    └── client.py
```

## Concepts Explored

- Creating TCP sockets with Python's built-in `socket` module.
- Binding a server socket to a port and listening for a connection.
- Accepting a client connection and exchanging byte streams.
- Working with IP addresses and TCP ports.
- Reading and writing data over a socket.
- Capturing process output using Python's `subprocess` module.
- Inspecting and changing the client's working directory.

## Technologies

| Module | Purpose in this experiment |
|---|---|
| `socket` | TCP socket creation and communication |
| `subprocess` | Process execution in the current client implementation |
| `os` | Working-directory operations |
| `sys` | Process exit handling in the server |

The code uses Python's standard library; no third-party packages are listed as dependencies.

## Current Implementation

- `server.py` binds to port `9999`, listens for a connection, and handles one client at a time.
- `client.py` connects to a server address hard-coded in the source (`192.168.1.5`) on port `9999`.
- The client executes received text as a shell command and sends captured output back over the connection.

The address is specific to the author's local network and will not work on every machine. The files are an experimental implementation, not a secure remote-management tool.

## Known Issues and Limitations

- **No authentication or encryption:** network traffic and commands are not protected.
- **Arbitrary command execution:** the client runs received input through a shell, creating a serious security risk.
- **Single-client design:** the server handles one accepted connection at a time.
- **Recursive bind retry:** a failed bind calls `bind_socket()` again recursively; if the port remains occupied, the process can eventually raise `RecursionError`.
- **Incomplete error handling:** connection failures and disconnects are not handled consistently.
- **No message framing:** TCP is a byte stream, so one `recv()` call is not guaranteed to return one complete application message.
- **Potential blocking:** socket reads and subprocess output reads can block.
- **Working-directory handling needs correction:** the client attempts to change directories but continues through the command-processing path afterward.
- **Hard-coded network configuration:** the client IP address is embedded in the source.

## Safe Development Direction

For a safer networking portfolio project, replace remote shell execution with a message-only protocol. Useful next steps include:

- Exchange text messages without executing them as operating-system commands.
- Add explicit message framing and socket timeouts.
- Handle disconnects and shutdown cleanly.
- Replace recursive retries with bounded error handling.
- Add tests for connection success, refused connections, and unexpected disconnects.
- If the project later handles sensitive data, design authentication and encrypted transport before implementing those features.

## Disclaimer

This repository is for educational study of Python networking concepts. Use only in an isolated lab with systems you own or are explicitly authorized to test. It is not production-ready and should not be treated as a secure remote-access solution.

## License

No license is specified in this repository. Add a license file if you intend to grant others permission to use, modify, or redistribute the code.
