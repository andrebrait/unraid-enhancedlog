<div align="center">

<img src="src/usr/local/emhttp/plugins/enhanced.log3/icons/enhanced.log3.png" alt="Enhanced Log v3 logo" width="96">

<h1>Enhanced Log v3</h1>

<p><strong>Advanced syslog filtering, colorization, and categorization for <a href="https://unraid.net/">Unraid</a>.</strong></p>

<p>
  <a href="https://github.com/andrebrait/unraid-enhancedlog/releases"><img src="https://img.shields.io/github/v/release/andrebrait/unraid-enhancedlog?label=release&color=blue" alt="Latest release"></a>
  <img src="https://img.shields.io/badge/Unraid-7.0%2B-e8543f" alt="Supported Unraid versions">
  <a href="https://github.com/andrebrait/unraid-enhancedlog/releases"><img src="https://img.shields.io/github/downloads/andrebrait/unraid-enhancedlog/total?color=blueviolet" alt="Downloads"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/andrebrait/unraid-enhancedlog?color=green" alt="License: GPL-3.0"></a>
</p>

</div>

## Fork notice

This is a maintained fork of [dkaser/unraid-enhancedlog](https://github.com/dkaser/unraid-enhancedlog) by Derek Kaser, based on the original work by Dan Landon. This fork carries on maintaining the plugin and publishes its own releases.

### Installation

In the Unraid web UI, go to **Plugins → Install Plugin** and enter:

```
https://raw.githubusercontent.com/andrebrait/unraid-enhancedlog/main/plugin/enhanced.log3.plg
```

Installing replaces the previous Enhanced Log plugin (the original `enhanced.log`, or an earlier release of this fork) and keeps your settings. The plugin was renamed to `enhanced.log3` ("Enhanced Log v3") so Community Applications can tell it apart from the original.

### Requirements

- Unraid 7.0.0 or later.

### Issues

Report bugs and feature requests in the [issue tracker of this fork](https://github.com/andrebrait/unraid-enhancedlog/issues).

## Overview

**Enhanced Log v3** is a powerful syslog enhancement plugin for Unraid, providing advanced log filtering, colorization, categorization, and analytics. It helps users quickly identify important system events, troubleshoot issues, and customize log viewing to their needs.

## Features

- **Advanced Filtering:** Filter syslog entries by category, keyword, or custom rules.
- **Colorization:** Assign colors to log lines based on severity or content for easier scanning.
- **Categorization:** Automatically group log entries (e.g., drive-related, file system, network).
- **Custom Match Rules:** Define your own patterns for highlighting or categorizing log lines.
- **Log Analytics:** View counts and trends for recurring log messages.
- **Persistent Settings:** All configuration is saved and restored across reboots.

## Configuration

Configuration files are stored in `/boot/config/plugins/enhanced.log3/`.  

## Development

### Requirements

- PHP 7.4+ (Unraid built-in)
- [Composer](https://getcomposer.org/) for dependency management

### Testing

1. Clone the repository.
2. Run `./composer install` to install dependencies.

### Release 

1. Use the provided GitHub Actions workflow for release automation.

Workflow actions use SHA-pinned versions of their latest available major releases. The custom release-drafter pin is retained because its conventional-commit changes are not on the upstream default branch. The PHP-CS-Fixer Docker action continues to track its `latest` image.

## Contributing

Pull requests and issues are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines, including code checks, commit message conventions, and licensing. You can also open an issue to discuss your idea.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).

> Portions copyright (C) 2015-2025 Dan Landon  
> Copyright (C) 2025 Derek Kaser

See [License.txt](License.txt) and [LICENSE](LICENSE) for details.

## Acknowledgements

- Based on original work by Dan Landon.
- Inspired by the Unraid syslog viewer and community feedback.

---

For the history of the original plugin, see the [Unraid forums thread](https://forums.unraid.net/topic/43115-enhanced-log-view-with-lines-highlighted-in-color/). For support, open an issue in the [issue tracker of this fork](https://github.com/andrebrait/unraid-enhancedlog/issues).
