# 🚀 Ruthishkumar G - AI & Full Stack Engineer Portfolio

[![Website](https://img.shields.io/badge/Website-Visit-blue?style=for-the-badge&logo=google-chrome)](https://ruthishkumar18.github.io/portfolio/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github)](https://github.com/ruthishkumar18)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/ruthishkumar18/)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=for-the-badge&logo=gmail)](mailto:ruthishkumarg@gmail.com)

> ### 🌟 **Live Demo:** [ruthishkumar18.github.io/portfolio](https://ruthishkumar18.github.io/portfolio/)

------------------------------------------------------------------------

## 📖 About This Portfolio

This is my personal portfolio website showcasing my journey as an **AI
Engineer** and **Full Stack Developer**. The website features my
projects, skills, experience, education, certifications, and a contact
form integrated with Google Forms.

### 🎯 Purpose

-   Showcase my AI/ML projects and full-stack development work
-   Provide a professional online presence for potential employers
-   Demonstrate my technical skills and achievements
-   Offer a way for recruiters to contact me

------------------------------------------------------------------------

## ✨ Features

-   🎨 **Modern Dark Theme** - Sleek, professional design with gradient
    accents
-   ⚡ **Interactive UI** - Smooth animations, particle effects, and
    typing animations
-   📱 **Fully Responsive** - Works on all devices (mobile, tablet,
    desktop)
-   🤖 **AI Projects Showcase** - Highlighting my work in Artificial
    Intelligence
-   📄 **Resume Download** - One-click download of my resume
-   📧 **Contact Form** - Integrated with Google Forms for easy
    communication
-   🔗 **Social Links** - Connect with me on LinkedIn, GitHub, and Email
-   🎯 **SEO Optimized** - Clean HTML with semantic elements

------------------------------------------------------------------------

## 🛠️ Technologies Used

### Frontend

-   **HTML5** - Semantic markup
-   **CSS3** - Custom styling with animations
-   **JavaScript** - Interactive elements and animations
-   **Google Fonts** - Space Grotesk, Syne, JetBrains Mono

### Design & Animations

-   Custom CSS variables for theming
-   CSS Grid & Flexbox for layouts
-   CSS animations (particles, typing effect, scroll animations)
-   Glass-morphism effects (backdrop-filter)

### Deployment

-   **GitHub Pages** - Hosting platform
-   **Google Forms** - Contact form backend

------------------------------------------------------------------------

## 📂 Project Structure

``` text
portfolio/
├── index.html              # Main HTML file
├── ruthish_resume.pdf      # Resume PDF
├── README.md               # This file
└── .github/
    └── workflows/          # GitHub Actions workflows
        └── pages.yml       # GitHub Pages deployment config
```

------------------------------------------------------------------------

## 🚀 Getting Started

### Prerequisites

-   A modern web browser
-   Git (for cloning)
-   Code editor (VS Code recommended)

### Local Development

1.  **Clone the repository**

    ``` bash
    git clone https://github.com/ruthishkumar18/portfolio.git
    cd portfolio
    ```

2.  **Open in browser**

    ``` bash
    # Simply open index.html in your browser
    open index.html
    # OR
    start index.html  # Windows
    ```

3.  **Make changes**

    -   Edit `index.html` to update content
    -   Modify styles in the `<style>` section
    -   Update JavaScript in the `<script>` section

4.  **Deploy to GitHub Pages**

    ``` bash
    git add .
    git commit -m "Update portfolio"
    git push origin main
    ```

------------------------------------------------------------------------

## 🔧 Customization Guide

### Update Personal Information

-   Search for "Ruthishkumar" in `index.html` and replace with your name
-   Update email addresses (`ruthishkumarg@gmail.com`)
-   Update social media links (LinkedIn, GitHub)
-   Replace project descriptions with your own

### Add/Modify Projects

``` html
<div class="proj-card">
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

``` html
<div class="skill-cat">
    <div class="skill-cat-icon">🚀</div>
    <h3>Category Name</h3>
    <div class="skill-tags">
        <span class="tag">Skill 1</span>
        <span class="tag">Skill 2</span>
        <span class="tag">Skill 3</span>
    </div>
</div>
```

### Configure Google Forms Integration

1.  Create a Google Form

2.  Find the form ID and entry IDs

3.  Update these lines in `index.html`:

    ``` javascript
    const GFORM_URL = 'https://docs.google.com/forms/d/e/YOUR_FORM_ID/formResponse';
    const ENTRY = {
        name: 'entry.YOUR_ENTRY_ID',
        email: 'entry.YOUR_ENTRY_ID',
        subject: 'entry.YOUR_ENTRY_ID',
        message: 'entry.YOUR_ENTRY_ID'
    };
    ```

------------------------------------------------------------------------

## 📱 Responsive Design

The portfolio is optimized for: - **Desktop** (1024px+) - **Tablet**
(768px - 1024px) - **Mobile** (320px - 768px)

------------------------------------------------------------------------

## 🌐 Deployment

### Deploy to GitHub Pages

1.  **Enable GitHub Pages**
    -   Go to repository Settings
    -   Navigate to Pages section
    -   Set source to `main` branch
    -   Save
2.  **Automatic Deployment**
    -   Every push to `main` branch triggers automatic deployment
    -   Site updates within 1-2 minutes
3.  **Custom Domain** (Optional)
    -   Add a `CNAME` file with your domain
    -   Configure DNS settings with your domain provider

### Manual Deployment

``` bash
# Build or prepare your files
# Then deploy using GitHub CLI
gh pages deploy
```

------------------------------------------------------------------------

## 🔍 SEO & Performance

### Meta Tags

``` html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Ruthishkumar G - AI Engineer & Full Stack Developer Portfolio">
<meta name="keywords" content="AI, Machine Learning, Full Stack, Developer, Portfolio">
<meta name="author" content="Ruthishkumar G">
```

### Performance Optimizations

-   Minimal external dependencies
-   Optimized CSS (inline critical styles)
-   Lazy loading for images
-   Efficient animations using CSS

------------------------------------------------------------------------

## 🤝 Contributing

This is a personal portfolio, but if you find any bugs or have
suggestions:

1.  Fork the repository
2.  Create your feature branch
    (`git checkout -b feature/AmazingFeature`)
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

------------------------------------------------------------------------

## 📄 License

This project is open source and available under the [MIT
License](LICENSE).

------------------------------------------------------------------------

## 📞 Contact

-   **Email:** <ruthishkumarg@gmail.com>
-   **LinkedIn:**
    [ruthishkumar18](https://www.linkedin.com/in/ruthishkumar18/)
-   **GitHub:** [ruthishkumar18](https://github.com/ruthishkumar18)
-   **Portfolio:**
    [ruthishkumar18.github.io/portfolio](https://ruthishkumar18.github.io/portfolio/)

------------------------------------------------------------------------

## 🙏 Acknowledgments

-   Google Fonts for the beautiful typography
-   GitHub Pages for free hosting
-   All the open-source tools and libraries used

------------------------------------------------------------------------

## 📊 Repository Statistics

![GitHub repo
size](https://img.shields.io/github/repo-size/ruthishkumar18/portfolio)
![GitHub last
commit](https://img.shields.io/github/last-commit/ruthishkumar18/portfolio)
![GitHub
stars](https://img.shields.io/github/stars/ruthishkumar18/portfolio?style=social)
![GitHub
forks](https://img.shields.io/github/forks/ruthishkumar18/portfolio?style=social)

------------------------------------------------------------------------

**⭐ If you like this portfolio, give it a star!** ⭐

------------------------------------------------------------------------

*Designed & Built with ❤️ by Ruthishkumar G*
