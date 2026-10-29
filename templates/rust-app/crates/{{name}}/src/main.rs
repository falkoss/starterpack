// SPDX-License-Identifier: {{licence}}
//! The command line of {{name}}: the terminal interface, the API with the web app, and the API's description.

use clap::{Parser, Subcommand};

use {{crate}}_app::Workspace;

/// {{tagline}}.
#[derive(Debug, Parser)]
#[command(name = "{{name}}", version)]
struct Cli {
    #[command(subcommand)]
    command: Command,
}

#[derive(Debug, Subcommand)]
enum Command {
    /// The terminal interface.
    Tui,
    /// The API and the web app on this device.
    Serve {
        /// The port on 127.0.0.1.
        #[arg(long, default_value_t = {{api_port}})]
        port: u16,
    },
    /// Prints the API's description in OpenAPI – what api/openapi.json holds.
    Openapi,
}

fn main() -> anyhow::Result<()> {
    match Cli::parse().command {
        Command::Tui => {{crate}}_tui::run(&mut Workspace::new())?,
        Command::Serve { port } => {
            let ready = |address: std::net::SocketAddr| println!("{{name}} at http://{address} – Ctrl-C ends");
            tokio::runtime::Runtime::new()?.block_on({{crate}}_api::serve(Workspace::new(), port, ready))?;
        }
        Command::Openapi => println!("{}", {{crate}}_api::openapi()),
    }
    Ok(())
}
