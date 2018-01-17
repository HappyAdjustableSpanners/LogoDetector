using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(LogoDetector.Startup))]
namespace LogoDetector
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
