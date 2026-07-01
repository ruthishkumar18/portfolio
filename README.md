# 🚀 Ruthishkumar G - AI & Full Stack Engineer Portfolio

[![Website](https://img.shields.io/badge/Website-Live-blue?style=for-the-badge&logo=google-chrome)](https://ruthishkumar18.github.io/portfolio/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github)](https://github.com/ruthishkumar18)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/ruthishkumar18/)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=for-the-badge&logo=gmail)](mailto:ruthishkumarg@gmail.com)

> ### 🌟 **Live Demo:** [ruthishkumar18.github.io/portfolio](https://ruthishkumar18.github.io/portfolio/)

---

## 📖 About This Portfolio

This is my **professional portfolio website** showcasing my journey as an **AI Engineer** and **Full Stack Developer**. The portfolio features a modern, responsive design with advanced animations, dark/light theme support, and interactive 3D elements.

### 🎯 Purpose
- Showcase my AI/ML projects and full-stack development work
- Provide a professional online presence for potential employers
- Demonstrate my technical skills and achievements
- Offer a seamless way for recruiters to contact me

---

## ✨ Key Features

### 🎨 Design & UI
- **Modern Dark Theme** with elegant purple/cyan gradients
- **Light Theme Support** with persistent preference storage
- **Fully Responsive** - Optimized for all devices (320px → 4K)
- **Glass-morphism Effects** with backdrop blur
- **Custom Typography** using Space Grotesk, Syne, JetBrains Mono
- **Smooth Color Transitions** between themes

### 🎬 Advanced Animations
- **Scroll-Triggered Reveals** with staggered delays (0.1s - 0.7s)
- **3D Card Tilt** - Cards follow cursor in real 3D space
- **Cursor Spotlight** - Dynamic glow following mouse
- **Typing Effect** on hero name
- **Floating Particles** in background
- **Scroll Progress Bar** with gradient
- **Back to Top Button** with smooth scroll
- **Hover Effects** - Shimmer, glow, scale, rotate
- **Pulsing Badges** with glow animations
- **Reduced Motion Support** for accessibility

### 🔧 Interactive Features
- **Theme Toggle** (Dark/Light) with localStorage persistence
- **Scroll-Spy Navigation** - Active link highlighting
- **Animated Statistics** - Numbers count up when scrolled into view
- **Resume Download** from Google Drive
- **Contact Form** integrated with Google Forms
- **Real-time Form Validation**
- **Success/Failure States** with feedback

### 📱 Mobile Optimization
- **Touch-Optimized** interactions
- **Reduced Animation Intensity** on mobile
- **Fewer Particles** for better performance
- **Responsive Grid** layouts
- **Collapsible Navigation** on small screens

---

## 🛠️ Technologies Used

### Frontend
- **HTML5** - Semantic, accessible markup
- **CSS3** - Custom properties, animations, 3D transforms
- **JavaScript (Vanilla)** - No frameworks, pure performance
- **Web Speech API** - For text-to-speech (future enhancement)
- **Google Fonts** - Space Grotesk, Syne, JetBrains Mono

### Design Features
- **CSS Variables** for theming
- **3D Transforms** with perspective
- **CSS Grid & Flexbox** for layouts
- **Custom Animations** (@keyframes)
- **Glass-morphism** (backdrop-filter)
- **Gradient Accents** throughout

### Performance & Accessibility
- **IntersectionObserver** for scroll animations
- **Preload** critical assets
- **Reduced Motion Media Query**
- **Semantic HTML** for screen readers
- **No External Dependencies** - Self-contained

### Deployment
- **GitHub Pages** - Free hosting
- **Google Forms** - Contact form backend
- **GitHub Actions** - Automated deployments

---

## 📂 Project Structure

```
portfolio/
├── index.html              # Complete portfolio (all-in-one)
├── ruthish_resume.pdf      # Resume PDF (optional)
├── README.md               # This documentation
└── .github/
    └── workflows/          # GitHub Actions
        └── pages.yml       # GitHub Pages deployment config
```

---

## 🚀 Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Safari, Edge)
- Git (for cloning)
- Any code editor (VS Code recommended)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/ruthishkumar18/portfolio.git
   cd portfolio
   ```

2. **Open in browser**
   ```bash
   # Simply open index.html in your browser
   open index.html
   # OR
   start index.html  # Windows
   # OR
   xdg-open index.html  # Linux
   ```

3. **Make changes**
   - Edit `index.html` to update content
   - Modify styles in the `<style>` section
   - Update JavaScript in the `<script>` section

4. **Deploy to GitHub Pages**
   ```bash
   git add .
   git commit -m "Update portfolio"
   git push origin main
   ```

---

## 🔧 Customization Guide

### Update Personal Information
- Search for "Ruthishkumar" in `index.html` and replace with your name
- Update email addresses (`ruthishkumarg@gmail.com`)
- Update social media links (LinkedIn, GitHub)
- Replace project descriptions with your own

### Add/Modify Projects
```html
<div class="proj-card featured animate-on-scroll delay-1">
    <div class="spotlight"></div>
    <div class="proj-img"><div class="proj-img-inner">🖥️</div></div>
    <div class="proj-body">
        <h3>Your Project Name</h3>
        <p>Brief description of your project</p>
        <div class="proj-tech">
            <span>Tech1</span>
            <span>Tech2</span>
            <span>Tech3</span>
        </div>
        <div class="proj-links">
            <a href="https://github.com/yourrepo" class="proj-link" target="_blank">
                <svg><!-- GitHub Icon --></svg>
                GitHub
            </a>
        </div>
    </div>
</div>
```

### Update Skills
```html
<div class="skill-cat animate-on-scroll delay-1">
    <div class="skill-cat-icon" style="background:linear-gradient(135deg,rgba(124,58,237,.3),rgba(79,70,229,.2))">🚀</div>
    <h3>Category Name</h3>
    <div class="skill-tags">
        <span class="tag">Skill 1</span>
        <span class="tag">Skill 2</span>
        <span class="tag">Skill 3</span>
    </div>
</div>
```

### Configure Google Forms Integration
1. Create a Google Form
2. Find the form ID and entry IDs:
   - Open the form in Chrome
   - Right-click → Inspect → Network tab
   - Submit a test form
   - Look for "formResponse" request
   - Copy the `entry.XXXXXXXXXX` IDs

3. Update these lines in `index.html`:
   ```javascript
   const GFORM_URL = 'https://docs.google.com/forms/d/e/YOUR_FORM_ID/formResponse';
   const ENTRY = {
       name: 'entry.YOUR_ENTRY_ID',
       email: 'entry.YOUR_ENTRY_ID',
       subject: 'entry.YOUR_ENTRY_ID',
       message: 'entry.YOUR_ENTRY_ID'
   };
   ```

### Customize Theme Colors
Edit the `:root` variables in CSS:
```css
:root{
  --c1:#0a0a0f;      /* Background dark */
  --c2:#0d0d1a;      /* Secondary dark */
  --c3:#111128;      /* Tertiary dark */
  --acc:#7c3aed;     /* Primary accent (purple) */
  --acc2:#06b6d4;    /* Secondary accent (cyan) */
  --acc3:#10b981;    /* Tertiary accent (green) */
  --text:#f0f0ff;    /* Text color */
  --muted:#8888aa;   /* Muted text */
}
```

---

## 📱 Responsive Design

The portfolio is optimized for:
- **4K & Ultra-wide** (2560px+)
- **Desktop** (1024px - 2560px)
- **Laptop** (768px - 1024px)
- **Tablet** (600px - 768px)
- **Mobile** (320px - 600px)

---

## 🌐 Deployment

### Deploy to GitHub Pages (Recommended)

1. **Enable GitHub Pages**
   - Go to repository Settings
   - Navigate to Pages section
   - Set source to `main` branch
   - Select `/ (root)` folder
   - Save

2. **Automatic Deployment**
   - Every push to `main` triggers deployment
   - Site updates within 1-2 minutes

3. **Custom Domain** (Optional)
   - Add a `CNAME` file with your domain
   - Configure DNS settings

### Manual Deployment Options
- **Netlify**: Drag-and-drop or connect GitHub
- **Vercel**: One-click import from GitHub
- **AWS S3**: Static website hosting
- **Any static hosting**: Upload the `index.html` file

---

## 🔍 SEO & Performance

### Meta Tags
```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Ruthishkumar G - AI Engineer & Full Stack Developer Portfolio">
<meta name="keywords" content="AI, Machine Learning, Full Stack, Developer, Portfolio">
<meta name="author" content="Ruthishkumar G">
```

### Performance Optimizations
- **Minimal external dependencies**
- **Optimized CSS** (inline critical styles)
- **Efficient animations** using transform/opacity
- **Lazy loading** for off-screen content
- **Reduced motion** support for accessibility
- **No external JavaScript libraries**

---

## 🎨 Animation System

### Scroll Animations
| Class | Effect |
|-------|--------|
| `.animate-on-scroll` | Fade up from bottom |
| `.delay-1` to `.delay-7` | Staggered delays (0.1s - 0.7s) |
| `.visible` | Triggered when in viewport |

### 3D Tilt System
- Cards tilt in 3D space following cursor
- Inner content lifts on separate Z-axis
- Spotlight glow follows cursor
- Max tilt: ±7 degrees

### Hover Effects
- **Cards**: Lift + glow + 3D tilt
- **Buttons**: Shimmer sweep
- **Tags**: Scale + color change
- **Icons**: Scale + rotate
- **Links**: Underline animation

---

## 🤝 Contributing

This is a personal portfolio, but if you find any bugs or have suggestions:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 📞 Contact

- **Email:** [ruthishkumarg@gmail.com](mailto:ruthishkumarg@gmail.com)
- **LinkedIn:** [ruthishkumar18](https://www.linkedin.com/in/ruthishkumar18/)
- **GitHub:** [ruthishkumar18](https://github.com/ruthishkumar18)
- **Portfolio:** [ruthishkumar18.github.io/portfolio](https://ruthishkumar18.github.io/portfolio/)

---

## 🙏 Acknowledgments

- **Google Fonts** - Beautiful typography
- **GitHub Pages** - Free hosting
- **All open-source tools** used in development
- **The open-source community** for inspiration

---

## 📊 Repository Statistics

![GitHub repo size](https://img.shields.io/github/repo-size/ruthishkumar18/portfolio)
![GitHub last commit](https://img.shields.io/github/last-commit/ruthishkumar18/portfolio)
![GitHub stars](https://img.shields.io/github/stars/ruthishkumar18/portfolio?style=social)
![GitHub forks](https://img.shields.io/github/forks/ruthishkumar18/portfolio?style=social)

---

## 🔮 Future Enhancements

- [ ] AI-powered avatar with speech
- [ ] Blog section for technical articles
- [ ] Interactive project demos
- [ ] Real-time visitor counter
- [ ] Performance analytics
- [ ] More 3D interactions

---

**⭐ If you like this portfolio, give it a star!** ⭐

---

*Designed & Built with ❤️ by Ruthishkumar G*
```

---

## 📝 How to Add This README

1. **Go to your repository:** `https://github.com/ruthishkumar18/portfolio`
2. **Click "Add file"** → **"Create new file"**
3. **Name the file:** `README.md`
4. **Copy and paste** the content above
5. **Scroll down** and click **"Commit new file"**

---

## 🎨 Optional: Add Badges to Header

Add this at the very top for a nicer badge header:

```markdown
[![Deploy to GitHub Pages](https://img.shields.io/badge/Deployed%20on-GitHub%20Pages-blue?style=for-the-badge&logo=github)](https://ruthishkumar18.github.io/portfolio/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
