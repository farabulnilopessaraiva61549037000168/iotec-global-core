/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: ['res.cloudinary.com', 'storage.googleapis.com', 'your-storage-domain.com']
  }
}
module.exports = nextConfig

