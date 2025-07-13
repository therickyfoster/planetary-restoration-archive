import { NFTStorage } from 'nft.storage';
import { filesFromPaths } from 'files-from-path';
import path from 'path';

const dir = 'public';

async function main() {
  const files = await filesFromPaths(['.'], { hidden: false });

  const client = new NFTStorage({ token: process.env.NFT_STORAGE_API_TOKEN });
  const cid = await client.storeDirectory(files);
  console.log('✅ Uploaded folder with CID:', cid);
}

main().catch(err => {
  console.error('❌ Upload failed:', err);
  process.exit(1);
});
