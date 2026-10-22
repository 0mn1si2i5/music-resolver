# music-resolver

把任意一条音乐链接（Spotify / Apple Music / 网易云音乐 / QQ 音乐链接，或带前后文的分享文案）解析成规范曲目，并补全另外三个平台的对应链接。

A small FastAPI service that turns a music link (Spotify, Apple Music, NetEase Cloud Music or QQ Music, or a share text containing one) into a canonical track and finds the matching links on the other three platforms.

从 [Side B](https://github.com/0mn1si2i5/Side-B) 的 `backend/` 拆出，保留了相关提交历史；房间、聊天、账号和 WebSocket 部分已移除，不再需要 `JWT_SECRET` 或数据库迁移。

## 使用方

- Pox（个人 agent）的每日推歌：给推荐的歌补全四个平台的链接。和 Pox 部署在同一台主机，只监听 `127.0.0.1:8788`。

## 接口

| 方法 | 路径 | 说明 |
|---|---|---|
| `GET` | `/health` | 健康检查 |
| `GET` | `/api/platforms` | 支持的平台 |
| `POST` | `/api/resolve` | `{rawLink, preferredMarket?, includePlatformLinks?}` → 规范曲目 + 平台链接（30/分钟） |
| `POST` | `/api/resolve-platform-links` | 已知规范曲目 → 全部平台链接（10/分钟） |
| `POST` | `/api/resolve-platform-link` | 已知规范曲目 → 单个平台链接（30/分钟） |

路径和端口与 Side B 后端完全一致，调用方切换时不需要改代码。

## 运行

```bash
cp .env.example .env    # 填 Spotify 凭证
uv venv -p 3.12 .venv && uv pip install -p .venv -r requirements-dev.txt
.venv/bin/python -m pytest -q
.venv/bin/python -m app.main
```

网易云解析依赖一个 NeteaseCloudMusicApi 服务（`NETEASE_API_BASE_URL`）；`docker compose up` 会一并启动。QQ 音乐通过 `qqmusic-api-python` 直连。平台链接缓存写在 `data/platform_link_cache.db`。

## 与 Side B 的对应关系

`git filter-repo` 改写了提交哈希。Side B 的 `e34a85f` 对应本仓库 `e32b758`，Side B 最后一个提交 `0dbe9f7` 对应本仓库 `9285301`。Side B 已归档，之后的改动只在本仓库进行。

## 许可证

[GPL-3.0-or-later](LICENSE)。运行时依赖 `qqmusic-api-python`（GPL-3.0-or-later），其他第三方说明见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
