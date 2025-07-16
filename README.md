# 神经网络研究数据展示平台

一个现代化的静态网站，用于展示和浏览神经网络研究数据。支持300+个神经网络模型的展示，包括训练结果、测试数据、程序代码和架构图示。

## 🚀 在线演示

[点击这里查看在线演示](https://your-deployment-url.vercel.app)

## ✨ 特性

- **响应式设计** - 适配桌面和移动设备
- **搜索功能** - 快速搜索神经网络模型
- **数据可视化** - 直观展示训练和测试结果
- **代码展示** - 完整的模型实现代码
- **架构图示** - SVG格式的网络架构图
- **统计信息** - 实时统计数据概览
- **现代UI** - 优雅的用户界面设计

## 🛠️ 技术栈

- **前端**: 纯HTML、CSS、JavaScript
- **样式**: 自定义CSS，响应式设计
- **数据**: JSON格式数据存储
- **部署**: Vercel静态托管

## 📦 项目结构

```
neural-network-gallery/
├── index.html          # 主页面
├── data.json          # 神经网络数据
├── package.json       # 项目配置
├── vercel.json        # Vercel部署配置
├── generate_data.py   # 数据生成脚本
└── README.md          # 项目说明
```

## 🚀 部署到Vercel

### 方法1: 通过Git仓库部署

1. 将项目上传到GitHub仓库
2. 登录 [Vercel](https://vercel.com)
3. 点击 "New Project"
4. 选择你的GitHub仓库
5. 配置项目设置：
   - Framework Preset: `Other`
   - Root Directory: `./` (或者你的项目目录)
   - Build Command: `echo "No build needed"`
   - Output Directory: `./`
6. 点击 "Deploy"

### 方法2: 通过Vercel CLI部署

1. 安装Vercel CLI:
```bash
npm install -g vercel
```

2. 在项目目录中运行:
```bash
vercel
```

3. 按照提示完成部署配置

### 方法3: 拖拽部署

1. 访问 [Vercel部署页面](https://vercel.com/new)
2. 将项目文件夹拖拽到部署区域
3. 等待部署完成

## 🔧 本地开发

1. 克隆项目到本地:
```bash
git clone your-repo-url
cd neural-network-gallery
```

2. 启动本地服务器:
```bash
# 使用Python
python -m http.server 8000

# 或使用Node.js
npx serve .

# 或使用PHP
php -S localhost:8000
```

3. 打开浏览器访问 `http://localhost:8000`

## 📊 数据格式

每个神经网络数据项包含以下字段：

```json
{
  "name": "网络名称",
  "result": {
    "train": "训练数据的CSV格式字符串",
    "test": "测试数据的CSV格式字符串"
  },
  "program": "完整的程序代码",
  "motivation": "研究动机描述",
  "svg_picture": "SVG格式的架构图",
  "index": 1000,
  "parent": 999
}
```

## 🎨 自定义

### 修改样式

编辑 `index.html` 中的 `<style>` 标签来自定义样式。

### 添加新数据

1. 编辑 `data.json` 文件
2. 或运行 `generate_data.py` 生成新数据
3. 重新部署到Vercel

### 修改配置

编辑 `vercel.json` 文件来修改部署配置。

## 📱 浏览器兼容性

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## 🤝 贡献

欢迎提交Issue和Pull Request来改善这个项目。

## 📄 许可证

MIT License

## 🔗 相关链接

- [Vercel文档](https://vercel.com/docs)
- [HTML5规范](https://html.spec.whatwg.org/)
- [CSS3规范](https://www.w3.org/Style/CSS/)
- [JavaScript MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

## 💡 常见问题

### Q: 如何添加更多神经网络数据？
A: 编辑 `data.json` 文件，按照现有格式添加新的数据项，然后重新部署。

### Q: 如何自定义主题颜色？
A: 修改 `index.html` 中的CSS变量，特别是颜色相关的样式。

### Q: 部署后页面显示空白？
A: 检查浏览器控制台是否有错误，确保 `data.json` 文件格式正确。

### Q: 如何修改页面标题？
A: 编辑 `index.html` 中的 `<title>` 标签和页面标题文本。

---

如果你觉得这个项目有用，请给个⭐️！ 