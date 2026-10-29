// SPDX-License-Identifier: {{licence}}
//! Where the data of {{name}} lives. Provisional: in memory, gone when the program ends – OPEN: SQLite (rusqlite) for
//! local-first, PostgreSQL (sqlx) for a server. Only `{{name}}-app` uses it.

use {{crate}}_core::Item;

/// Why the store could not do what was asked.
#[derive(Debug, thiserror::Error)]
pub enum StoreError {
    /// No item with this id.
    #[error("no item {0}")]
    NotFound(u64),
}

/// The items, in the order they were added.
#[derive(Debug, Default)]
pub struct Store {
    items: Vec<Item>,
    next: u64,
}

impl Store {
    /// An empty store.
    pub fn new() -> Self {
        Self::default()
    }

    /// Keeps a new item with a checked title and gives it the next id.
    pub fn insert(&mut self, title: String) -> Item {
        self.next += 1;
        let item = Item { id: self.next, title };
        self.items.push(item.clone());
        item
    }

    /// Every item.
    pub fn items(&self) -> &[Item] {
        &self.items
    }

    /// Takes an item out.
    pub fn remove(&mut self, id: u64) -> Result<Item, StoreError> {
        let at = self.items.iter().position(|item| item.id == id).ok_or(StoreError::NotFound(id))?;
        Ok(self.items.remove(at))
    }
}
