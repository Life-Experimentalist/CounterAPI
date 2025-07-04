# Changelog

All notable changes to CounterAPI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0]() - 2025-07-04

### Added
- `/health` endpoint for proper database connectivity testing
- Real-time connection status testing in the frontend settings modal
- Enhanced connection testing that actually verifies database connectivity
- Count editing capability in the project edit functionality

### Improved
- Connection testing now uses proper health check endpoint instead of unreliable table existence checks
- Better error handling and user feedback for connection issues
- Project editing now allows updating name, description, AND count values
- Updated Postman collection with corrected endpoints and health check request
- Enhanced documentation to reflect health check capabilities and count editing
- Render deployment configuration now uses proper `/health` endpoint for health checks

### Fixed
- Corrected Postman collection endpoints to match actual API routes
- Fixed DELETE endpoint to use RESTful path parameters
- Fixed PING endpoint to use correct `/projects/ping` route
- Removed unreliable database connection status indicators

### Fixed
- Removed unreliable connection status indicators that gave false positives/negatives
- Fixed Postman collection endpoints to match actual API routes
- Corrected DELETE endpoint to use proper RESTful path parameter
- Fixed ping endpoint URL in Postman collection

### Updated
- Documentation updated to include `/health` endpoint
- Architecture diagrams updated to show health check system
- USAGE.md updated with health check examples

## [1.0.0]() - 2025-06-27

### Added
- Initial release of CounterAPI
- Core FastAPI backend with full CRUD operations for projects
- PostgreSQL database integration with schema support
- Interactive dashboard with glassmorphism design
- Real-time project statistics and live updates
- Environment auto-detection (Render vs GitHub Pages vs local)
- Settings modal with API configuration and connection testing
- Database schema viewer showing tables, columns, and connection status
- Debounced project reloading for seamless UI updates
- Responsive mobile-friendly design
- Dark Reader extension compatibility
- One-click deployment to Render.com
- `/meta` endpoint for deployment and database information
- Proper error handling for database connection failures
- Support for project descriptions
- Smooth animations and transitions throughout the UI
- Comprehensive documentation (README, USAGE, ARCHITECTURE)

### API Endpoints
- `GET /projects` - List all projects with counts and descriptions
- `POST /projects` - Add a new project
- `PUT /projects?name={name}` - Update project name/description
- `DELETE /projects/{name}` - Delete a project
- `POST /projects/ping` - Increment project count
- `GET /health` - Check API and database connectivity status
- `GET /meta` - View deployment and database info
- `GET /` - Serve interactive dashboard

### Technical Features
- FastAPI backend with async/await support
- PostgreSQL with psycopg2-binary driver
- CORS middleware for cross-origin requests
- Static file serving for the dashboard
- Environment variable configuration
- Graceful database connection error handling
- Dynamic connection status detection
- Python-dotenv support for local development

### UI Features
- Modern glassmorphism design with CSS variables
- Real-time statistics display
- Project tile management with smooth animations
- Settings modal with connection testing
- Database schema visualization
- Toast notifications for user feedback
- Fade-in/fade-out transitions
- Responsive grid layout
- Icon-based project cards
- Debounced reload mechanism (5-second window)

### Documentation
- Comprehensive README with deployment instructions
- Quick usage guide with curl examples
- Architecture documentation with Mermaid diagrams
- TODO list for future enhancements
- Postman collection for API testing
- Database setup instructions for Filess.io
