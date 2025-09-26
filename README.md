# PySide Todo App

A modern desktop todo application built with PySide6 (Qt for Python) and SQLAlchemy, featuring a clean Material Design-inspired interface.

## Features

- **Modern UI**: Clean, dark-themed interface inspired by Microsoft To Do
- **Task Management**: Add, complete, and delete tasks
- **Database Storage**: SQLite database with SQLAlchemy ORM
- **Responsive Layout**: Sidebar navigation with main content area
- **Search Functionality**: Search through your tasks
- **Multiple Lists**: Support for different task categories (My Day, Important, Planned, etc.)

## Screenshots

The application features a two-panel layout:
- **Left Sidebar**: Navigation menu with task categories and search
- **Main Content**: Task input and list display

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd pyside-todo-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python main.py
```

### Basic Operations

- **Add a Task**: Type in the input field and click "Add Task" or press Enter
- **Complete a Task**: Check the checkbox next to a task
- **Delete a Task**: Click the "X" button on a task item
- **Search Tasks**: Use the search box in the sidebar

## Project Structure

```
pyside-todo-app/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── toto.db                # SQLite database (auto-generated)
├── core/
│   └── database.py        # Database configuration and initialization
├── models/
│   └── todo.py           # SQLAlchemy models (Task, TaskList)
├── ui/
│   ├── main_window.py    # Main application window
│   ├── sidebar.py        # Left sidebar component
│   ├── content.py        # Main content area
│   ├── task_item.py      # Individual task widget
│   └── task_title_search_box.py  # Search component
└── resources/            # Static resources (if any)
```

## Technologies Used

- **PySide6**: Qt-based GUI framework for Python
- **SQLAlchemy**: SQL toolkit and ORM
- **SQLite**: Lightweight database engine
- **Python 3.13**: Programming language

## Dependencies

- `PySide6>=6.7.0` - GUI framework
- `qtawesome>=1.3.0` - Icon library
- `SQLAlchemy>=2.0.0` - Database ORM
- `pytest>=8.0.0` - Testing framework (optional)
- `pyinstaller>=6.0.0` - Build executable (optional)

## Database Schema

The application uses two main tables:

- **TaskList**: Contains task categories/lists
- **Task**: Individual tasks with title, completion status, and timestamps

## Building Executable

To create a standalone executable:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

## Development

### Running Tests

```bash
pytest
```

### Code Structure

- **Models**: Database models using SQLAlchemy ORM
- **UI Components**: Modular PySide6 widgets
- **Database**: SQLite with SQLAlchemy for data persistence
- **Architecture**: MVC-like pattern with separation of concerns

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Future Enhancements

- [ ] Task due dates and reminders
- [ ] Task categories and tags
- [ ] Import/Export functionality
- [ ] Sync with cloud services
- [ ] Dark/Light theme toggle
- [ ] Task priority levels
- [ ] Drag and drop task reordering

## Troubleshooting

### Common Issues

1. **Database not found**: The database file `toto.db` is automatically created on first run
2. **Module not found**: Ensure all dependencies are installed with `pip install -r requirements.txt`
3. **GUI not displaying**: Make sure PySide6 is properly installed and your system supports Qt

### System Requirements

- Windows 10/11, macOS 10.14+, or Linux
- Python 3.8+
- 50MB free disk space
- 4GB RAM (recommended)

## Contact

For questions or suggestions, please open an issue in the repository.